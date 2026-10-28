numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))
