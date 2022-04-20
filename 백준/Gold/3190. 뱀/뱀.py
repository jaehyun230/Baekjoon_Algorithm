from collections import deque
import sys
input = sys.stdin.readline
#판 크기
n = int(input())
#사과 개수
k = int(input())
#방향 전환 정보 리스트
direction_list = deque()
#뱀의 위치
snake = deque()
#게임판
graph = [[0]*(n+1) for _ in range(n+1)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(k) :
  y, x = map(int, input().split())
  #사과 위치정보 추가
  graph[y][x] = 2

#방향 전환 정보 개수
l = int(input())

for _ in range(l) :
  time, direction = input().split()
  #방향 전환 정보 추가
  direction_list.append((int(time), direction))

play_time = 0
change_time = int(1e9)
now = 2

#뱀 머리 위치
head = [1, 1]
snake.append((1, 1))
while True :
  if direction_list :
    change_time = direction_list[0][0]
  else :
    change_time = int(1e9)
  if change_time == play_time :
    if direction_list[0][1] == "L" :
      now -=1
      if now < 0 :
        now = 3
    else :
      now +=1
      if now > 3 :
        now = 0
    direction_list.popleft()

  play_time +=1
  
  head[0], head[1] = head[0]+dy[now], head[1]+dx[now]
  
  snake.append((head[0], head[1]))
  #벽을 부딛힐 경우
  if head[0] > n or head[0] < 1 or head[1] > n or head[1] < 1 :
    break
  #자기 몸통에 부딛힐 경우
  elif graph[head[0]][head[1]] == 1 :
    break
  #빈공간으로 이동할 경우
  elif graph[head[0]][head[1]] == 0 :
    graph[head[0]][head[1]] = 1
    tail = snake.popleft()
    graph[tail[0]][tail[1]] = 0
  #사과를 먹은 경우 
  elif graph[head[0]][head[1]] == 2 :
    graph[head[0]][head[1]] = 1
  
print(play_time)