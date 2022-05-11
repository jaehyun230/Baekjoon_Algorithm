import heapq
import sys

input = sys.stdin.readline

n = int(input())

left_num = []
right_num = []

for _ in range (n) :
  x = int(input())
  if x <= 0 :
    heapq.heappush(left_num, x)
  else :
    heapq.heappush(right_num, -x)

answer = 0
while len(left_num) >=2 :
  num1 = heapq.heappop(left_num)
  num2 = heapq.heappop(left_num)
  answer += num1 * num2
  
while len(right_num) >=2 :
  num1 = heapq.heappop(right_num) * -1
  num2 = heapq.heappop(right_num) * -1
  if num1 == 1 or num2 == 1 :
    answer += num1 + num2
  else :
    answer += num1 * num2

if left_num :
  answer += heapq.heappop(left_num)
if right_num :
  answer += heapq.heappop(right_num) * -1

print(answer)