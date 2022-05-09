import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

q = []

for _ in range (n) :
  x, y = map(int, input().split())
  heapq.heappush(q, ((x, y)))

#가방 무게저장
bag = [int(input()) for _ in range(k)]

bag.sort()

temp = []

answer = 0
for w in bag :
  
  while q and w >= q[0][0] :
    weight, price = heapq.heappop(q)
    heapq.heappush(temp, -price)
    
  if temp :
    answer -= heapq.heappop(temp)
  elif not q:
    break

print(answer)