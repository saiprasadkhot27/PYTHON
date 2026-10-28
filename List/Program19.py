students = ["Rahul", "Priya", "Amit", "Sneha"]

print("Total students present:", len(students))

name = input("Enter student name to search: ")

if name in students:
    print(name, "is present.")
else:
    print(name, "is absent.")

new_student = input("Enter new student name: ")
students.append(new_student)
print("After adding:", students)

absent_student = input("Enter absent student name to remove: ")

if absent_student in students:
    students.remove(absent_student)
    print("After removing:", students)
else:
    print("Student not found.")
