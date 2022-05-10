import heapq
import sys

input = sys.stdin.readline

n= int(input())

left_q = []
right_q = []

for _ in range (n) :
  x = int(input())
  if len(left_q) == len(right_q) :
    #가장 큰 값을 앞에 나두기 위해서 *-1
    heapq.heappush(left_q, -x)
  else :
    heapq.heappush(right_q, x)

  #left_q 최대값이 right_q 최소값보다 작으면 교체
  if left_q and right_q and left_q[0] * -1 > right_q[0] :
    max_value = heapq.heappop(left_q)
    min_value = heapq.heappop(right_q)
        
    heapq.heappush(left_q, min_value * -1)
    heapq.heappush(right_q, max_value * -1)
  #중간값
  print(left_q[0] * -1)