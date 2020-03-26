a=int(input())
arr = list(map(int, input().split()))
cnt=0
for i in range(0, a):
    if arr[i]>0:
        cnt+=1
print(cnt)