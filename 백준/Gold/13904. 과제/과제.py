import heapq
import sys

input = sys.stdin. readline

n = int(input())

q = []

for _ in range (n) :
  x, y = map(int, input().split())
  heapq.heappush(q, (x, y))

my_time = 0
stack = []

while q :
  day, score  = heapq.heappop(q)
  if day > len(stack) :   
    heapq.heappush(stack, (score))
  else :
    if score > stack[0] :
      heapq.heappop(stack)
      heapq.heappush(stack, score)
      
print(sum(stack))