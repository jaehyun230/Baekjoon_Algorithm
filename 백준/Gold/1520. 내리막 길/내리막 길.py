import sys
sys.setrecursionlimit(10 **8)
input = sys.stdin.readline



def dfs(x, y) :

  if x == n-1 and y == m-1 :
    return 1

  if visited[x][y] != -1 :
    return visited[x][y]

  way = 0
  for i in range(4) :
    mx = x+dx[i]
    my = y+dy[i]
    if 0 <= mx < n and 0 <= my < m :
      if graph[x][y] > graph[mx][my] :
        way += dfs(mx, my)

  visited[x][y] = way
  return visited[x][y]

n, m = map(int, input().split())

graph = []

for _ in range(n) :
  graph.append(list(map(int, input().split())))

visited = [[-1]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
     
print(dfs(0,0))