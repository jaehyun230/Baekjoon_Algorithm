from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().rstrip())) for _ in range (n)]

q = deque()
q.append((0, 0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

INF = int(1e9)
visited = [[INF]* n for _ in range (n)]
visited[0][0] = 0
answer = []
while q :
  x, y, c = q.popleft()
  if x == n-1 and y == n-1 :
    answer.append(c)
    continue
  for i in range (4) :
    mx = x+dx[i]
    my = y+dy[i]
    if 0 <= mx < n and 0 <= my < n :
      if graph[mx][my] == 0 and visited[mx][my] > c+1:
        
        visited[mx][my] = c+1
        q.append((mx, my, c+1))
      elif graph[mx][my] == 1 and visited[mx][my] > c:
        
        visited[mx][my] = c
        q.append((mx, my, c))

print(min(answer))