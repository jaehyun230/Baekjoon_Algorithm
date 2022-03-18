from collections import deque
import copy

# 시간초과로 pypy로 수행하여야 함
def bfs() :
  queue = deque()
  temp_graph = copy.deepcopy(graph)

  for i in range (n) :
    for j in range (m) :
      if temp_graph[i][j] == 2 :
        queue.append((i, j))

  while queue :
    x, y = queue.popleft()
    for i in range (4) :
      mx = x + dx[i]
      my = y + dy[i]

      if 0<= mx < n and 0<= my < m :
        if temp_graph[mx][my] == 0 :
          temp_graph[mx][my] = 2
          queue.append((mx, my))

  global max_num
  num = 0        
  for i in range(n):
    num += temp_graph[i].count(0)
  max_num = max(max_num, num)
          
def wall(counts):
  if counts == 3 :
    bfs()
    return

  for i in range (n) :
    for j in range (m) :
      if graph[i][j] == 0 :
        graph[i][j] = 1
        wall(counts+1)
        graph[i][j] = 0

n, m = map(int,input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_num = 0
counts = 0

for i in range (n) :
  graph.append(list(map(int, input().split())))
  
wall(0)
print(max_num)
