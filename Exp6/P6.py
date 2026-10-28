file = open("sample.txt", "r")

lines = file.readlines()

print("Number of lines:", len(lines))

file.close()