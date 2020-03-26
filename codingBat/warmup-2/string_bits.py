def string_bits(str):
  s_new=""
  for i in range(len(str)):
    if i%2==0:
      s_new+=str[i]
      
  return s_new