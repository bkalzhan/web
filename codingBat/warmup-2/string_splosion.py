def string_splosion(str):
  s_new=""
  for i in range(len(str)):
    s_new+=str[:i+1]
  return s_new