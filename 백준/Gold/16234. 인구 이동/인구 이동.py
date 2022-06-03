from collections import deque
import sys
input = sys.stdin.readline

graph = []

n, l, r = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j) :
  q = deque()
  q.append([i, j])
  temp = []
  temp.append([i, j])
  while q :
    x, y = q.popleft()
    for i in range(4) :
      mx = x + dx[i]
      my = y + dy[i]
      if 0 <= mx < n and 0 <= my < n and visited[mx][my] == 0 :
        if l <= abs(graph[x][y] - graph[mx][my]) <= r :
          visited[mx][my] = 1
          temp.append([mx, my])
          q.append([mx, my])
          
  return temp

for _ in range (n) :
  graph.append(list(map(int, input().split())))

time = 0

while True :
  visited = [[0]*n for _ in range(n)]
  move_time = False
  for i in range(n) :
    for j in range(n) :
      if visited[i][j] == 0 :
        visited[i][j] = 1
        temp = bfs(i, j)
        if len(temp) > 1 :
          move_time = True
          average = sum([graph[x][y] for x, y in temp]) // len(temp)
          for x, y in temp :
            graph[x][y] = average
  if move_time == False :
    break
  time +=1
  
print(time)