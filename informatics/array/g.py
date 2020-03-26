a=int(input())
arr = list(map(int, input().split()))
cnt=0

arr.reverse()
for i in range(0, a):
    print(arr[i])