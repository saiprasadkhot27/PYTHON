import math

n = int(input())
r = int(math.sqrt(n))

if r < 2:
    print("Not Prime")
else:
    prime = True
    for i in range(2, int(math.sqrt(r)) + 1):
        if r % i == 0:
            prime = False
            break
    if prime:
        print("Prime")
    else:
        print("Not Prime")