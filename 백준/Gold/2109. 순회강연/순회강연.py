import heapq
import sys

input = sys.stdin.readline

n = int(input())

lecture = []
heap = []

for _ in range (n) :
  p, d = map(int, input().split())
  lecture.append((p, d))

lecture.sort(key = lambda x:x[1])

for cost, day in lecture :
  heapq.heappush(heap, cost)
  if day < len(heap) :
    heapq.heappop(heap)

print(sum(heap))