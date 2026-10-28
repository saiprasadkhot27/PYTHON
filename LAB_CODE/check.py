
T1 = (10, "PYTHON", 30, 40.56)

print("Tuple:", T1)
print("Address:", id(T1))
print("Type:", type(T1))


T1 = list(T1)
T1.append(12)
T1.append("Coder")
print("\nAfter conversion:")
print("List:", T1)
print("Address:", id(T1))
print("Type:", type(T1))
