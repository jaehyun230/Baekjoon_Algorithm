from collections import deque

n = int(input())

graph = []

for _ in range (n) :
  graph.append(list(map(int, input().split())))

visited = [[0]*n for _ in range(n)]
#시작 시점
visited[0][0] = 1

for i in range (n) :
  for j in range (n) :
    if visited[i][j] != 0 :
      if i == n-1 and j == n-1 :
        break
      if i+graph[i][j] < n :
        visited[i+graph[i][j]][j] += visited[i][j]
      if j+graph[i][j] < n :
        visited[i][j+graph[i][j]] += visited[i][j]

print(visited[n-1][n-1])