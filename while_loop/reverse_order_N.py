p = True
q = False

print("Propositional Logic")
print("P AND Q:", p and q)
print("P OR Q:", p or q)
print("NOT P:", not p)
print("P implies Q:", (not p) or q)

numbers = [1, 2, 3, 4, 5]

print("\nPredicate Logic")
print("All numbers are positive:", all(x > 0 for x in numbers))
print("At least one number is even:", any(x % 2 == 0 for x in numbers))