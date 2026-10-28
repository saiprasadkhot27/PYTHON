scores = [120, 45, 78, 101, 56, 34, 150, 67, 89, 95]

highest = scores[0]
lowest = scores[0]
total = 0
centuries = 0
half_centuries = 0

for score in scores:
    total += score

    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

    if score >= 100:
        centuries += 1

    if score >= 50 and score < 100:
        half_centuries += 1

average = total / len(scores)

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Number of centuries:", centuries)
print("Number of half-centuries:", half_centuries)
