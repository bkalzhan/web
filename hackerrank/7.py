n = int(input())
arr = list(map(int, input().split()))
arr.sort()
k=arr[arr.__len__()-1]
min2=-101
for i in range(0, n):
    if arr[i]>min2 and arr[i]<k:
        min2=arr[i]

print(min2)
