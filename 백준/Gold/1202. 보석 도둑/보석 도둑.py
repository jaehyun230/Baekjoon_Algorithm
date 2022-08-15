import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

jewel = []

for _ in range (n) :
  a, b = map(int, input().split())
  heapq.heappush(jewel, (a, b))

bag = [int(input()) for _ in range(k)]
bag.sort()

answer = 0
temp = []
for w in bag :

  while jewel and w >= jewel[0][0] :
    weight, price = heapq.heappop(jewel)
    heapq.heappush(temp, (-price))

  if temp :
    answer -= heapq.heappop(temp)
  elif not jewel :
    break

print(answer)