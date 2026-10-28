add = lambda n: 0 if n == 0 else n + add(n - 1)

print(add(5))
