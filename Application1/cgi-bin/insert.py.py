#!C:/Python313/python.exe

import cgi

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

name = form.getvalue("name")
mobile = form.getvalue("mobile")
email = form.getvalue("email")
age = form.getvalue("age")

with open("data.txt", "a") as file:
    file.write(f"{name},{mobile},{email},{age}\n")

print("""
<html>
<body>
<h2>Data Inserted Successfully!</h2>
<a href="/">Back</a>
</body>
</html>
""")