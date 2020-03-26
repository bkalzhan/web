def missing_char(str, n):
  s_new=""
  for i in range(len(str)):
    if i==n:
      continue
    s_new+=str[i]
  
  return s_new