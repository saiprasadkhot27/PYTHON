from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=50,
        label="Username",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter username'
            }
        )
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter email'
            }
        )
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password'
            }
        )
    )

    mobile = forms.CharField(
        label="Mobile Number",
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message="Enter a valid 10-digit Indian mobile number."
            )
        ],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter mobile number'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']

        if not username.isalnum():
            raise ValidationError(
                "Username must contain only letters and numbers."
            )

        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 8:
            raise ValidationError(
                "Password must contain at least 8 characters."
            )

        if not any(char.isupper() for char in password):
            raise ValidationError(
                "Password must contain at least one uppercase letter."
            )

        if not any(char.isdigit() for char in password):
            raise ValidationError(
                "Password must contain at least one number."
            )

        return password