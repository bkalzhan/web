def front_times(str, n):
  s_new=""
  front=str
  if len(str)>3:
    front=str[:3]
  for i in range(n):
    s_new+=front
  return s_new
