list1 = [10, 20, 30, 40, 50]

print("Original list:", list1)

list1.append(60)
print("append:", list1)

list1.extend([70, 80])
print("extend:", list1)

list1.insert(2, 25)
print("insert:", list1)

list1.remove(40)
print("remove:", list1)

x = list1.pop()
print("pop:", list1)
print("popped element:", x)

x = list1.pop(2)
print("pop(index):", list1)
print("popped element:", x)

print("Index of 30:", list1.index(30))

list1.append(30)
print("Count of 30:", list1.count(30))

list1.sort()
print("sort:", list1)

list1.sort(reverse=True)
print("sort(reverse=True):", list1)


list1.reverse()
print("reverse:", list1)

list2 = list1.copy()
print("copy:", list2)

list1.clear()
print("clear:", list1)

list1 = [1, 2, 3, 4, 5]

print("Length:", len(list1))
print("Maximum:", max(list1))
print("Minimum:", min(list1))
print("Sum:", sum(list1))


print("Membership:", 3 in list1)

print("Not membership:", 10 not in list1)



print("Reverse slicing:", list1[::-1])

list2 = [6, 7, 8]
list3 = list1 + list2
print("Concatenation:", list3)

list4 = list1 * 2
print("Repetition:", list4)


print("First element:", list1[0])
print("Last element:", list1[-1])
