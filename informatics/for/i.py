import math

a=int(input())
cnt=0
b=int(math.sqrt(a))

for i in range (1, b):
    if a%i==0:
        cnt+=1

cnt*=2

if b*b==a:
    cnt+=1

print(cnt)