def last2(str):
  cnt=0
  last=str[-2:]
  for i in range(len(str)-1):
    if str[i:2+i]==last:
      cnt+=1
      
  if cnt>0:
    return cnt-1
  return 0