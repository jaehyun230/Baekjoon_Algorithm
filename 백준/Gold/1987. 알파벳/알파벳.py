import sys

input = sys.stdin.readline

graph = []
alpha = set()

global answer
answer = 1

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range (n) :
  data = list(input().rstrip())
  graph.append(data)

def dfs(x,y, cost) :
  global answer
  answer = max(answer, cost)
  
  for i in range(4) :
    mx = x+dx[i]
    my = y+dy[i]
    if 0<= mx < n and 0<= my < m :
      if graph[mx][my] not in alpha :
        alpha.add(graph[mx][my])
        dfs(mx, my, cost+1)
        alpha.remove(graph[mx][my])

alpha.add(graph[0][0])
dfs(0,0, 1)
print(answer)