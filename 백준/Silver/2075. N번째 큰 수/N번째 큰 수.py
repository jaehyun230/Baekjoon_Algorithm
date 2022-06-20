import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []
for _ in range (n) :
  nums = list(map(int, input().split()))

  for i in nums :
    if len(q) < n :
      heapq.heappush(q, i)
    else :
      if q[0] < i :
        heapq.heappop(q)
        heapq.heappush(q, i)

print(q[0])