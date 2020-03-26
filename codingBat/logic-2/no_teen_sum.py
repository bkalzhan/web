def no_teen_sum(a, b, c):
  sum=0
  if not fix_teen(a):
    sum+=a
  if not fix_teen(b):
    sum+=b
  if not fix_teen(c):
    sum+=c
  return sum




def fix_teen(n):
  if n==15 or n==16:
    return False
  elif n>=13 and n<=19:
    return True
  return False
    