a=int(input())
arr = list(map(int, input().split()))
array=''
for i in range(0, a):
    if i%2==0:
        array+=f'{arr[i]} '
print(array)