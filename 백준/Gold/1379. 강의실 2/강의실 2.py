import heapq

import sys

input = sys.stdin.readline

n = int(input())

q = []
arr = []

lecture = [0] * (n+1)

for _ in range(n) :
  num, start, end = map(int, input().split())
  arr.append([start, end, num])

arr.sort()

answer = 0

for s, e, idx in arr :
  if q and q[0][0] <= s :
    lecture[idx] = lecture[q[0][2]]
    heapq.heappop(q)
  else :
    answer +=1
    lecture[idx] = answer

  heapq.heappush(q, [e, s, idx])

print(answer)

for i in range(1, len(lecture)) :
  print(lecture[i])