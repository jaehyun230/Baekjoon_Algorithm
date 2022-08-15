import heapq
import sys

input = sys.stdin.readline

n = int(input())

answer = 0

q = []
heap = []

for _ in range (n) :
  _, a, b = map(int, input().split())
  heapq.heappush(q, (a, b))

while q :
  start, end = heapq.heappop(q)
  while heap :
    if heap[0] <= start :
      heapq.heappop(heap)
    else :
      break
  heapq.heappush(heap, (end))
  answer = max(answer, len(heap))
  
print(answer)