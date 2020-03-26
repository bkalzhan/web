a=int(input())
arr = list(map(int, input().split()))
cnt=0
for i in range(0, a-1):
    if (arr[i]>0 and arr[i+1]>0) or (arr[i]<0 and arr[i+1]<0):
        print('YES')
        cnt+=1
        break

if cnt==0:
    print('NO')