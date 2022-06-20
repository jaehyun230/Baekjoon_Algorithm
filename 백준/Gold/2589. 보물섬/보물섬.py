from collections import deque
import sys

input = sys.stdin.readline

def bfs(a,b) :
  q = deque()
  q.append((a, b, 0))
  visited = [[0] * (m) for _ in range (n)]
  dist = 0
  visited[a][b] = 1
  while q :
    x, y, c = q.popleft()
    dist = max(dist, c)
    for i in range (4) :
      mx = x + dx[i]
      my = y + dy[i]
      if 0 <= mx < n and 0 <= my < m and graph[mx][my] == "L" and visited[mx][my] == 0 :
        visited[mx][my] = 1
        q.append((mx, my, c+1))

  return dist
    

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = [input().rstrip() for _ in range (n)]

answer = 0
for i in range (n) :
  for j in range (m) :
    if graph[i][j] == 'L' :
      answer = max(answer, bfs(i, j))

print(answer)