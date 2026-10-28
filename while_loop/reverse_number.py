n=int(input("enter a number"))
sum=0
rev=" "
origional_number=n

while n>0:
    rev=rev+ str(n%10)
    n=n//10

print(rev)
