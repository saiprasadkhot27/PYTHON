import os

directory = "NewFolder"

if os.path.exists(directory):
    os.rmdir(directory)
    print("Directory deleted successfully.")
else:
    print("Directory does not exist.")