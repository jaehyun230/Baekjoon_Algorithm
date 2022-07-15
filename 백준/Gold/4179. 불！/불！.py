from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(n)]

visited = [[False] * len(graph[0]) for _ in range (len(graph))]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

flag = True

for i in range(len(graph)) :
  for j in range(len(graph[0])) :
    if graph[i][j] == 'F' :
      q.append((i, j, -1))

for i in range(len(graph)) :
  for j in range(len(graph[0])) :
    if graph[i][j] == 'J' :
      q.append((i, j, 1))

while q :
  x, y, c = q.popleft()
  
  if c == -1 :
    for i in range(4) :
      mx = x+dx[i]
      my = y+dy[i]
      if 0 <= mx < len(graph) and 0 <= my < len(graph[0]) and graph[mx][my] != '#' and graph[mx][my] != 'F' :
        graph[mx][my] = 'F'
        q.append((mx, my, -1))

  else :
    if x == 0 or x == len(graph)-1 or y == 0 or y == len(graph[0])-1 :
      print(c)
      flag = False
      break
    
    for i in range(4) :
      mx = x+dx[i]
      my = y+dy[i]
      
      if 0 <= mx < len(graph) and 0 <= my < len(graph[0]) and graph[mx][my] =='.' :
        if visited[mx][my] == False :
          visited[mx][my] = True
          q.append((mx, my, c+1))

if flag :
  print("IMPOSSIBLE")