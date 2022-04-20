from collections import deque

#상자 가로 세로
m, n = map(int, input().split())
graph = []

for _ in range(n) :
  tomato = list(map(int, input().split()))
  graph.append(tomato)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs() :
  q = deque()
  for i in range(n) :
    for j in range(m) :
      if graph[i][j] == 1 :
        q.append((i, j))
  
  while q :
    y, x = q.popleft()
    for i in range(len(dx)) :
      mx = x+dx[i]
      my = y+dy[i]
      if mx >=0 and mx < m and my >=0 and my < n :
        if graph[my][mx] == 0 :
          graph[my][mx] = graph[y][x] + 1
          q.append((my, mx))
  time = 1
  for i in range(n) :
    for j in range(m) :
      if graph[i][j] == 0 :
        return -1
      elif time < graph[i][j] :
        time = graph[i][j]
        
  return time-1

print(bfs())