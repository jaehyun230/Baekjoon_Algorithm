import sys

input = sys.stdin.readline

from collections import deque

n, q = map(int, input().split())
graph = [[] for _ in range (n+1)]

for _ in range(n-1) :
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

for _ in range(q) :
  k, start = map(int, input().split())
  q = deque()
  q.append(start)
  visited = [0] *(n+1) 
  visited[start] = 1
  
  count = 0
  while q :
    now = q.popleft()
    for i in range (len(graph[now])) :
      if graph[now][i][1] >= k and visited[graph[now][i][0]] == 0:
        q.append(graph[now][i][0])
        visited[graph[now][i][0]] = 1
        count +=1
  print(count)