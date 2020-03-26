def end_other(a, b):
  a=a.lower()
  b=b.lower()
  if len(a)>len(b):
    return a[-len(b):]==b
  return b[-len(a):]==a