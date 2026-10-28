numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = 0

for num in numbers:
    total += num

average = total / 10

print("Sum:", total)
print("Average:", average)
