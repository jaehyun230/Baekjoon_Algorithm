from collections import deque
import sys

input = sys.stdin.readline
#가로 세로 높이
m, n, h = map(int, input().split())

need_time = 0
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

graph = []

for _ in range (h) :
  box = []
  for _ in range (n) :
    tomato = list(map(int, input().split()))
    box.append(tomato)
  graph.append(box)

q = deque()
for k in range (h) :
  for i in range(n) :
    for j in range(m) :
      if graph[k][i][j] == 1 :
        q.append((k, i, j))

while q :
  z, y, x = q.popleft()
  for i in range (len(dx)) :
    a = x+dx[i]
    b = y+dy[i]
    c = z+dz[i]
    if a>=0 and a<m and b>=0 and b< n and c >=0 and c <h :
      if graph[c][b][a] == 0 :
        graph[c][b][a] = graph[z][y][x] + 1
        q.append((c, b, a))

time = 0
for k in graph :
  for i in k :
    if 0 in i :
      print(-1)
      exit()
    else :
      time = max(time, max(i))
#time 기본 시작 1에서 퍼지기떄문에 -1
print(time-1)
      