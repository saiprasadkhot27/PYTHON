matrix1 = [
    [1, 21, 3],
    [4, 5, 61],
    [7, 18, 9]
]

matrix2 = [
    [9, 8, 7],
    [62, 4, 4],
    [36, 2, 2]
]

result = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Matrix Addition:")

for row in result:
    print(row)
