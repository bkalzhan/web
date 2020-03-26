def sum67(nums):
  block=False
  sum=0
  for n in nums:
    if n==6:
      block=True
      continue
    if n==7 and block:
      block=False
      continue
    if not block:
      sum+=n
  return sum