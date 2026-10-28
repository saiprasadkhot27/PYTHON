students = [
    ("Rahul", 80),
    ("Amit", 95),
    ("Priya", 75),
    ("Neha", 90)
]

students.sort(key=lambda x: x[1])

print(students)