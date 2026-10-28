from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
import easyocr
from PIL import Image
import sqlite3
import datetime
from functools import wraps
import re
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traceLens.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)

# Initialize OCR Reader (do this once)
reader = easyocr.Reader(['en'], gpu=False)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    expenses = db.relationship('Expense', backref='user', lazy=True, cascade='all, delete-orphan')

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    shop_name = db.Column(db.String(120), nullable=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50), default='Other')
    description = db.Column(db.Text, nullable=True)
    image_filename = db.Column(db.String(120), nullable=True)
    raw_text = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

# Login decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Image preprocessing for better OCR
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None
    
    # Resize image for better processing
    height, width = img.shape[:2]
    if width > 1920:
        ratio = 1920 / width
        new_height = int(height * ratio)
        img = cv2.resize(img, (1920, new_height))
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    
    # Apply thresholding
    _, thresh = cv2.threshold(enhanced, 150, 255, cv2.THRESH_BINARY)
    
    return thresh

# Extract amount from text using regex
def extract_amount(text):
    # Look for currency patterns
    patterns = [
        r'₹\s*(\d+(?:,\d{3})*(?:\.\d{2})?)',
        r'(?:total|amount|price|cost)[\s:]*₹\s*(\d+(?:,\d{3})*(?:\.\d{2})?)',
        r'(\d+(?:,\d{3})*(?:\.\d{2})?)\s*₹',
    ]
    
    text_lower = text.lower()
    for pattern in patterns:
        match = re.search(pattern, text_lower)
        if match:
            amount_str = match.group(1).replace(',', '')
            try:
                return float(amount_str)
            except:
                pass
    
    # If no pattern found, look for largest number
    numbers = re.findall(r'\d+(?:\.\d{2})?', text)
    if numbers:
        try:
            return float(max(numbers, key=lambda x: float(x)))
        except:
            pass
    
    return 0.0

# Extract date from text
def extract_date(text):
    date_patterns = [
        r'(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})',
        r'(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{2,4})',
    ]
    
    for pattern in date_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                if len(match.groups()) == 3:
                    day, month, year = match.groups()
                    if isinstance(month, str):
                        months = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                                 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
                        month = months.get(month.lower()[:3], 1)
                    else:
                        month = int(month)
                    
                    day = int(day)
                    year = int(year)
                    
                    if year < 100:
                        year += 2000
                    
                    date_obj = datetime(year, month, day).date()
                    return date_obj
            except:
                pass
    
    return datetime.now().date()

# Extract shop name
def extract_shop_name(text):
    lines = text.split('\n')
    # Usually shop name is in first few lines
    for line in lines[:5]:
        cleaned = line.strip()
        if len(cleaned) > 3 and len(cleaned) < 60:
            return cleaned
    return "Unknown Shop"

# Categorize expense
def categorize_expense(text, shop_name):
    text_lower = text.lower()
    shop_lower = shop_name.lower()
    
    categories = {
        'Grocery': ['dmart', 'grocery', 'supermarket', 'walmart', 'food', 'market', 'bhat'],
        'Restaurant': ['restaurant', 'cafe', 'pizza', 'burger', 'food court', 'hotel', 'dhaba', 'biriyani'],
        'Fuel': ['petrol', 'fuel', 'diesel', 'gas station', 'pump'],
        'Medical': ['pharmacy', 'medicine', 'hospital', 'clinic', 'medical', 'drug'],
        'Transport': ['auto', 'taxi', 'bus', 'train', 'metro', 'parking'],
        'Entertainment': ['movie', 'cinema', 'theater', 'game', 'play'],
        'Utilities': ['electricity', 'water', 'internet', 'phone', 'bill'],
        'Shopping': ['clothes', 'dress', 'shoe', 'mall', 'store', 'shop'],
    }
    
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in text_lower or keyword in shop_lower:
                return category
    
    return 'Other'

# Routes
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not username or not email or not password:
            return jsonify({'success': False, 'message': 'All fields required'}), 400
        
        if User.query.filter_by(username=username).first():
            return jsonify({'success': False, 'message': 'Username already exists'}), 400
        
        if User.query.filter_by(email=email).first():
            return jsonify({'success': False, 'message': 'Email already exists'}), 400
        
        user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Registration successful'}), 201
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            return jsonify({'success': True, 'message': 'Login successful'}), 200
        
        return jsonify({'success': False, 'message': 'Invalid username or password'}), 401
    
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    user_id = session['user_id']
    expenses = Expense.query.filter_by(user_id=user_id).order_by(Expense.created_at.desc()).all()
    
    total_spent = sum(e.amount for e in expenses) if expenses else 0
    month_spent = sum(e.amount for e in expenses 
                     if e.date.month == datetime.now().month and 
                     e.date.year == datetime.now().year) if expenses else 0
    
    return render_template('dashboard.html', 
                         expenses=expenses, 
                         total_spent=total_spent,
                         month_spent=month_spent,
                         expense_count=len(expenses))

@app.route('/upload', methods=['POST'])
@login_required
def upload_receipt():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No file selected'}), 400
    
    if not file.filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
        return jsonify({'success': False, 'message': 'Only image files allowed'}), 400
    
    try:
        # Save uploaded file
        filename = secure_filename(f"{datetime.now().timestamp()}_{file.filename}")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Preprocess image
        processed_image = preprocess_image(filepath)
        
        if processed_image is None:
            return jsonify({'success': False, 'message': 'Failed to process image'}), 400
        
        # Save processed image temporarily
        temp_processed = os.path.join(app.config['UPLOAD_FOLDER'], f"processed_{filename}")
        cv2.imwrite(temp_processed, processed_image)
        
        # Run OCR
        results = reader.readtext(temp_processed)
        extracted_text = '\n'.join([text[1] for text in results])
        
        # Extract information
        shop_name = extract_shop_name(extracted_text)
        amount = extract_amount(extracted_text)
        date = extract_date(extracted_text)
        category = categorize_expense(extracted_text, shop_name)
        
        # Create expense record
        user_id = session['user_id']
        expense = Expense(
            user_id=user_id,
            shop_name=shop_name,
            amount=amount,
            date=date,
            category=category,
            image_filename=filename,
            raw_text=extracted_text
        )
        
        db.session.add(expense)
        db.session.commit()
        
        # Cleanup temporary processed image
        os.remove(temp_processed)
        
        return jsonify({
            'success': True,
            'message': 'Receipt processed successfully',
            'data': {
                'id': expense.id,
                'shop_name': shop_name,
                'amount': amount,
                'date': str(date),
                'category': category,
                'confidence': 'High'
            }
        }), 201
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error processing receipt: {str(e)}'}), 500

@app.route('/api/expenses')
@login_required
def get_expenses():
    user_id = session['user_id']
    category = request.args.get('category', 'all')
    
    query = Expense.query.filter_by(user_id=user_id)
    
    if category != 'all':
        query = query.filter_by(category=category)
    
    expenses = query.order_by(Expense.date.desc()).all()
    
    return jsonify([{
        'id': e.id,
        'shop_name': e.shop_name,
        'amount': e.amount,
        'date': str(e.date),
        'category': e.category,
        'description': e.description
    } for e in expenses])

@app.route('/api/expense/<int:expense_id>', methods=['GET', 'DELETE', 'PUT'])
@login_required
def manage_expense(expense_id):
    user_id = session['user_id']
    expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first()
    
    if not expense:
        return jsonify({'success': False, 'message': 'Expense not found'}), 404
    
    if request.method == 'DELETE':
        # Delete image file if exists
        if expense.image_filename:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], expense.image_filename)
            if os.path.exists(image_path):
                os.remove(image_path)
        
        db.session.delete(expense)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Expense deleted'}), 200
    
    if request.method == 'PUT':
        data = request.get_json()
        expense.shop_name = data.get('shop_name', expense.shop_name)
        expense.amount = data.get('amount', expense.amount)
        expense.date = datetime.strptime(data.get('date', str(expense.date)), '%Y-%m-%d').date()
        expense.category = data.get('category', expense.category)
        expense.description = data.get('description', expense.description)
        
        db.session.commit()
        return jsonify({'success': True, 'message': 'Expense updated'}), 200
    
    # GET
    return jsonify({
        'id': expense.id,
        'shop_name': expense.shop_name,
        'amount': expense.amount,
        'date': str(expense.date),
        'category': expense.category,
        'description': expense.description,
        'raw_text': expense.raw_text,
        'image_filename': expense.image_filename
    })

@app.route('/api/analytics')
@login_required
def get_analytics():
    user_id = session['user_id']
    expenses = Expense.query.filter_by(user_id=user_id).all()
    
    # Category-wise spending
    category_spending = {}
    for expense in expenses:
        category_spending[expense.category] = category_spending.get(expense.category, 0) + expense.amount
    
    # Monthly spending (last 6 months)
    monthly_spending = {}
    for i in range(6):
        date = datetime.now() - timedelta(days=30*i)
        month_key = date.strftime('%Y-%m')
        monthly_spending[month_key] = 0
    
    for expense in expenses:
        month_key = expense.date.strftime('%Y-%m')
        if month_key in monthly_spending:
            monthly_spending[month_key] += expense.amount
    
    return jsonify({
        'category_spending': category_spending,
        'monthly_spending': dict(reversed(sorted(monthly_spending.items()))),
        'total_spent': sum(e.amount for e in expenses),
        'average_expense': sum(e.amount for e in expenses) / len(expenses) if expenses else 0
    })

@app.route('/analytics')
@login_required
def analytics_page():
    return render_template('analytics.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/api/search')
@login_required
def search_expenses():
    user_id = session['user_id']
    query = request.args.get('q', '')
    
    expenses = Expense.query.filter_by(user_id=user_id).filter(
        db.or_(
            Expense.shop_name.ilike(f'%{query}%'),
            Expense.description.ilike(f'%{query}%'),
            Expense.raw_text.ilike(f'%{query}%')
        )
    ).order_by(Expense.date.desc()).all()
    
    return jsonify([{
        'id': e.id,
        'shop_name': e.shop_name,
        'amount': e.amount,
        'date': str(e.date),
        'category': e.category
    } for e in expenses])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)