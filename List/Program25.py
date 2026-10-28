numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for item in numbers:
    if item not in unique:
        unique.append(item)

print(unique)
