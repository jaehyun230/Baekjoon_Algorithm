import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

def dfs(x, y) :
  if y == m-1 :
    return True
  for i in range(3) :
    if 0 <= x+dx[i] < n and graph[x+dx[i]][y+1] == '.' and visited[x+dx[i]][y+1] == False :
      visited[x+dx[i]][y+1] = True
      if dfs(x+dx[i], y+1) :
        return True
        
  return False
  

for _ in range (n) :
  data = list(input().rstrip())
  graph.append(data)

visited = [[False] * (m) for _ in range (n)]
dx = [-1, 0, 1]
answer = 0

for i in range(n) :
  if graph[i][0] == '.' :
    if dfs(i, 0) :
      answer +=1

print(answer)