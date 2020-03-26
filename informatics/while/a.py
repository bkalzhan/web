import math

n=int(input())
i=1

while i<=n:
    a=int(math.sqrt(i))
    if a**2==i:
        print(i)
    i+=1