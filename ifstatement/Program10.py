status = input("Marital Status (married/unmarried): ")
gender = input("Gender (male/female): ")
age = int(input("Enter age: "))

if status == "married":
    print("Driver is Insured")
elif status == "unmarried" and gender == "male" and age > 30:
    print("Driver is Insured")
elif status == "unmarried" and gender == "female" and age > 25:
    print("Driver is Insured")
else:
    print("Driver is Not Insured")