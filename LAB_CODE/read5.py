lines = '''Hello i am Saiprasad.
A b.tech 3rd year student.
I am curretly doing dsa in java.'''

count = 0

for i in lines.splitlines():
    if not i.startswith("T"):
        count += 1

print(count)
