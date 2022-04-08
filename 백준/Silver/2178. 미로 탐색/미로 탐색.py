from collections import deque

n, m = map(int, input().split())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * m for i in range(n)]

for i in range (n) :
  graph.append(list(map(int, input())))

q = deque()
q.append((0, 0))

while q :
  y, x = q.popleft()
  for i in range (len(dx)) :
    mx = x+dx[i]
    my = y+dy[i]
    if mx>=0 and mx <m and my >=0 and my < n :
      if graph[my][mx] == 1 :
        graph[my][mx] = graph[y][x] + 1
        q.append((my, mx))

print(graph[n-1][m-1])