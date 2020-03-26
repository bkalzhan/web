a=int(input())
i=1
k=0
while i<=a:
    if i==a:
        k+=1
        print("YES")
        break
    i*=2

if k==0:
    print("NO")