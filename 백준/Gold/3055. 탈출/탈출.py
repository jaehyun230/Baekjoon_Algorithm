from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
#맵
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y) :
  q = deque()
  # 웅덩이 추가
  for i in range (r) :
    for j in range (c) :
      if graph[i][j] == '*' :
        q.append((i, j, -1))
  visited = [[0]* c for _ in range (r)]
  visited[start_x][start_y] = 1
  q.append((start_x, start_y, 0))

  while q :
    # d = -1 인경우 웅덩이
    x, y, d = q.popleft()
    if graph[x][y] == 'D' :
      return d
    for i in range (4) :
      mx = x+dx[i]
      my = y+dy[i]
      if 0<= mx < r and 0<= my < c and graph[mx][my] != 'X' and visited[mx][my] == 0 :
        if d == -1 :
          if graph[mx][my] != 'D' :
            q.append((mx, my, -1))
            visited[mx][my] = 1
        else :
          q.append((mx, my, d+1))
          visited[mx][my] = 1
  #도착못하는경우        
  return -1

for _ in range (r) :
  graph.append(list(input().rstrip()))

for i in range (r) :
  for j in range (c) :
    if graph[i][j] == 'S' :
      answer = bfs(i, j)
      break

if answer == -1 :
  print("KAKTUS")
else :
  print(answer)