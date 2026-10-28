import os

items = os.listdir(".")

print("Files and directories:")

for item in items:
    print(item)