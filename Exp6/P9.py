import os

old_name = "sample.txt"
new_name = "new_sample.txt"

os.rename(old_name, new_name)

print("File renamed successfully.")