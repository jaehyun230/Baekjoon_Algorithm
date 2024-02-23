import heapq
import sys

input = sys.stdin.readline
n = int(input())

q = []

for _ in range(n) :
  start, end = map(int, input().split())
  heapq.heappush(q, (start, end))

q2 = []

answer = 0
while q :
  s, e = heapq.heappop(q)
  while q2 :
    if q2[0] <= s :
      heapq.heappop(q2)
    else :
      break
  heapq.heappush(q2, e)
  answer = max(answer, len(q2))
print(answer)