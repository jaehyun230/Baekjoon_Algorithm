import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rsplit()))
lis = []

answer = 0

for num in arr :
  if not lis :
    lis.append(num)
    answer +=1
  elif lis[-1] < num :
    lis.append(num)
    answer +=1
  else :
    index = bisect_left(lis, num)
    lis[index] = num

print(answer)