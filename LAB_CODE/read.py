file = open("story.txt", "r")

count = 0

for line in file:
    if line.startswith("T"):
        count = count + 1

print(count)

file.close()
