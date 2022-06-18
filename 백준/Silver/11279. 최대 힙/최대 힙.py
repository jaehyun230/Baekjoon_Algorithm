import heapq
import sys

input = sys.stdin.readline

n = int(input())

heap = []
for _ in range (n) :
  x = int(input())
  if x != 0 :
    heapq.heappush(heap, -x)

  elif x == 0 :
    if heap :
      out = heapq.heappop(heap)
      print(-out)
    else :
      print(0)