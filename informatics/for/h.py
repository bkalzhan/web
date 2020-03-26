a=int(input())

array=''

for i in range(1, a+1):
    if a%i==0:
        array+=f'{i} '

print(array)