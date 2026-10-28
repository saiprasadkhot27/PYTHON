salaries = [25000, 35000, 45000, 55000, 60000, 28000, 75000, 48000, 52000, 30000]

highest = salaries[0]
lowest = salaries[0]
total = 0
above_50000 = 0
below_30000 = 0

for salary in salaries:
    total += salary

    if salary > highest:
        highest = salary

    if salary < lowest:
        lowest = salary

    if salary > 50000:
        above_50000 += 1

    if salary < 30000:
        below_30000 += 1

average = total / len(salaries)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees earning above ₹50,000:", above_50000)
print("Employees earning below ₹30,000:", below_30000)
