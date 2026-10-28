import os

directory = "MyFolder"

if os.path.isdir(directory):
    print("Directory exists.")
else:
    print("Directory does not exist.")