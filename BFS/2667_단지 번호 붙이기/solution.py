from collections import deque
#땅 크기
N = int(input())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#단지별 집수 리스트
house = []

def bfs(i,j) :
  queue = deque()
  queue.append((i,j))

  count = 1
  while queue :
    a, b = queue.popleft()
    for k in range (4) :
      if 0 <= a+dx[k] < N and 0 <= b+dy[k] < N :
        if graph[a+dx[k]][b+dy[k]] == 1 :
          graph[a+dx[k]][b+dy[k]] = 0
          queue.append((a+dx[k], b+dy[k]))
          count +=1
          
  house.append(count)
for _ in range (N) :
  graph.append(list(map(int, input())))


for i in range (N) :
  for j in range (N) :
    if graph[i][j] == 1 :
      graph[i][j] = 0
      bfs(i,j)

#오름차순으로 정렬
house.sort()
print(len(house))
for i in house :
  print(i)
  
