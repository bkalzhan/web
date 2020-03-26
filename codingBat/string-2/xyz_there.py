def xyz_there(str):
  cnt=0
  for i in range (len(str)-2):
    if str[i:i+3]=="xyz":
      if i>0:
        if str[i-1:i]!=".":
          cnt+=1
      else:
        cnt+=1
  return cnt>0