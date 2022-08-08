import sys

input = sys.stdin.readline

l = int(input())

nums = list(map(int, input().split()))

n = int(input())

nums.sort()

if n in nums :
  print(0)

else :

  high = 0
  low = 0
  for i in range (len(nums)) :
    if nums[i] < n :
      low = nums[i]
    elif nums[i] > n and high == 0 :
      high = nums[i]

  high -=1
  low +=1

  print((n-low)* (high-n+1) + (high-n))


