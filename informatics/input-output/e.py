v=int(input())
t=int(input())

s=(v*t)%109

if s<0:
    print(s+109)
else:
    print(s)