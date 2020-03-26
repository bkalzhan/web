def centered_average(nums):
  nums.sort()
  sum=0
  cnt=0
  for i in range(1, len(nums)-1):
    cnt+=1
    sum+=nums[i]
  return sum//cnt