def sum2(nums):
  sum=0
  l=len(nums)
  if l>2:
    l=2
  for i in range(l):
    sum+=nums[i]
  return sum