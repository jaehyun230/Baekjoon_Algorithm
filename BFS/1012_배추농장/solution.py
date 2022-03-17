from collections import deque

#농장 갯수
N = int(input())
#이동 경우의 수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
count = 0
def bfs(i, j) :
  queue = deque()
  queue.append((i,j))

  while queue :
    a, b = queue.popleft()
    
    for k in range (len(dx)) :
      if a+dx[k] < n and a+dx[k] >=0 and b+dy[k] < m and b+dy[k] >= 0 :
        if graph[a+dx[k]][b+dy[k]] == 1 :
          graph[a+dx[k]][b+dy[k]] = 0
          queue.append((a+dx[k], b+dy[k]))
        
for _ in range(N) :
  #배추농장크기, 배추개수
  m,n,k = map(int, input().split())
  graph = [[0]* m for i in range (n)]
  for i in range(k):
    count = 0
    a,b = map(int, input().split())
    graph[b][a] = 1

  for i in range(n):
    for j in range(m) :
      if graph[i][j] == 1 :
        graph[i][j] = 0
        bfs(i, j)
        count +=1  

  print(count)
