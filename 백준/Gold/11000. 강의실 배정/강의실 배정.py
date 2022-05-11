import sys
import heapq

input = sys.stdin.readline

n = int(input())

lesson = []

for _ in range (n) :
  x, y = map(int, input().split())
  heapq.heappush(lesson, (x, y))

room = []
answer = 0
while lesson :
  start, end = heapq.heappop(lesson)
  flag = False
  if room :
    time = heapq.heappop(room)
    if time <= start :
        flag = True
        heapq.heappush(room, end)
    else :
      heapq.heappush(room, time)
      
  if flag == False :
    heapq.heappush(room, end)
    answer +=1

print(answer)