import sys

input = sys.stdin.readline

n = int(input())

building = list(map(int, input().split()))

def count_left(index) :
  min_slope = 10**10
  count = 0

  for i in range(index-1, -1, -1) :
    slope = (building[index] - building[i]) / (index-i)
    if min_slope > slope :
      min_slope = slope
      count +=1

  return count
      
def count_right(index) :
  max_slope = 10**10 * -1
  count = 0

  for i in range(index+1, n) :
    slope = (building[index] - building[i]) / (index-i)
    if max_slope < slope :
      max_slope = slope
      count +=1

  return count

answer = 0
for i in range (n) :
  answer = max(answer, count_left(i) + count_right(i))

print(answer)