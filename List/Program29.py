temperatures = [32, 35, 31, 29, 36, 34, 30, 33, 37, 28,
                31, 35, 39, 32, 30, 27, 34, 36, 38, 29,
                33, 31, 35, 40, 32, 28, 30, 37, 34, 36]

hottest = temperatures[0]
coldest = temperatures[0]
total = 0

for temperature in temperatures:
    total += temperature

    if temperature > hottest:
        hottest = temperature

    if temperature < coldest:
        coldest = temperature

average = total / len(temperatures)

above_average = 0
below_average = 0

for temperature in temperatures:
    if temperature > average:
        above_average += 1

    if temperature < average:
        below_average += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average temperature:", above_average)
print("Days below average temperature:", below_average)
