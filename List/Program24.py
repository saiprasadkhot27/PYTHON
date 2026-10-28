numbers = [1, 2, 3, 4, 5]

left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]

print("Left rotation:", left)
print("Right rotation:", right)
