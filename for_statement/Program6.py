x = float(input())
n = int(input())
s = 1
fact = 1
sign = -1
for i in range(2, n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    s += sign * (x ** i) / fact
    sign *= -1
print(s)