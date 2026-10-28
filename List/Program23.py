numbers = [1, 2, 2, 3, 1, 2, 4, 3, 3]

frequency = {}

for item in numbers:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)
