from collections import deque

n = int(input())

graph = []
for _ in range (n) :
  graph.append(list(map(int, input().split())))

maxh = 0
answer = []
for i in graph :
  if maxh < max(i) :
    maxh = max(i)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x1, y1, h):
    q = deque()
    q.append((x1, y1))
    visited[y1][x1] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx] and graph[ny][nx] > h:
                    visited[ny][nx] = True
                    q.append((nx, ny))

#비가 안오는경우도 있어서 0부터 시작
for h in range(maxh) :
  visited = [[False] * n for _ in range(n)]
  count = 0
  for i in range(n) :
    for j in range(n) :
      if not visited[i][j] and graph[i][j] > h :
        bfs(j, i, h)
        count +=1
  answer.append(count)

print(max(answer))