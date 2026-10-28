file = open("sample.txt", "r")

data = file.read()

words = data.split()

print("Number of words:", len(words))

file.close()