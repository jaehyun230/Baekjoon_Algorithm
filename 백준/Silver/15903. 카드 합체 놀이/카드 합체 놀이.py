import heapq

n, m = map(int, input().split())

num = list(map(int, input().split()))

heap = []
for i in num :
  heapq.heappush(heap, i)

while m != 0 :
  x1 = heapq.heappop(heap)
  x2 = heapq.heappop(heap)
  x = x1+x2
  for i in range (2) :
    heapq.heappush(heap, x)
  m -=1

print(sum(heap))