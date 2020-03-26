def array_front9(nums):
  l=len(nums)
  if len(nums)>4:
    l=4
  for i in range(l):
    if nums[i]==9:
      return True
  return False