import sys

input = sys.stdin.readline

import heapq

q = []

n = int(input())

for _ in range (n) :
  x = int(input())
  if x == 0 :
    if len(q) > 0 :
      val = heapq.heappop(q)
      print(val)
    else :
      print(0)
  else :
    heapq.heappush(q, x)