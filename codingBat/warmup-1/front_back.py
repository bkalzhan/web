def front_back(str):
  if len(str)<=1:
    return str
  
  mid=str[1:-1]
  return str[len(str)-1]+mid+str[0]

print(front_back("Bekzat"))