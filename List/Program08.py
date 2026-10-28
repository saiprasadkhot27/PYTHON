numbers = [10, 15, 22, 33, 40, 51, 64, 77, 80, 91, 12, 25, 36, 49, 58]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
