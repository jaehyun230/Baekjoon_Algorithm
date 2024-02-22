from collections import deque

def dfs(s) :
  print(s, end = " ")
  visited[s] = 1
  for i in graph[s] :
    if visited[i] == False :
      dfs(i)
  
  
  return

def bfs(s) :
  q = deque()
  q.append(s)
  visited = [False] * (n+1)
  visited[s] = True
  while q :
    now = q.popleft()
    print(now, end = " ")
    for go in graph[now] :
      if visited[go] == False :
        q.append(go)
        visited[go] = True

  return
    

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
for i in range(1, n+1) :
  graph[i].sort()

visited = [False] * (n+1)
dfs(v)
print()
bfs(v)