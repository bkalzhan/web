def make_chocolate(small, big, goal):
  n=goal//5
  if big>=n:
    goal=goal-5*n
  else:
    goal=goal-5*big
  
  if goal<=small:
    return goal
  return -1