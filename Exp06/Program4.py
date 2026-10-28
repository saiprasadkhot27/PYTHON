import os

directory = "PythonLab"

if not os.path.exists(directory):
    os.mkdir(directory)
    print("Directory created.")
else:
    print("Directory already exists.")

print("Current Directory:", os.getcwd())

print("Files and Folders:")

for item in os.listdir():
    print(item)