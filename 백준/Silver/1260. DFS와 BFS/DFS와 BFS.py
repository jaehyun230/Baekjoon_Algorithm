from collections import deque

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range (m) :
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

#edge 가는방향 오름차순 정렬
for i in range(1, n+1):
    graph[i].sort()

def dfs(start) :
  print(start, end = " ")
  visited[start] = 1
  for i in graph[start] :
    if visited[i] == 0 :
      dfs(i)
 
def bfs(graph, start) : 
  q = deque()
  q.append(start)
  visited = [0] * (n+1)
  visited[start] = 1

  while q :
    now = q.popleft()
    print(now, end = " ")
    for i in graph[now] :
      if visited[i] == 0 :
        visited[i] = 1
        q.append(i)

visited = [0] * (n+1)
dfs(start)
print()
bfs(graph, start)

