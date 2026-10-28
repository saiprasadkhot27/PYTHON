marks=[78,67,89,67,90,44,54,34,75,45,75,86,99,79,56,56,67,67,56,45]
length=len(marks)
print(length)
avg = sum(marks) / len(marks)

uavg=bavg=0
highest=lowest=marks[0]
for mark in marks:
    if mark>highest:
        highest=mark
    if mark<lowest:
        lowest=mark
    if mark>avg:
        uavg+=1
    if mark<avg:
        bavg+=1
        
    
print(highest)
print(lowest)

print("Number of student who marks is above avarage:",uavg)
print("Number of student who  marks is below average",bavg)




