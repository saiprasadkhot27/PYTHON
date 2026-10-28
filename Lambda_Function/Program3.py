file = open("sample.txt", "w")
file.write("Hello, World!")
file.close()

file = open("sample.txt", "r")
print(file.read())
file.close()
