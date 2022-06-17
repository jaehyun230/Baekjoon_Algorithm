import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [list(map(int ,input().split())) for _ in range (n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y) :
  global answer
  if dp[x][y] != 0 :
    return dp[x][y]
  dp[x][y] = 1
  
  for k in range (4) :
    mx = x+dx[k]
    my = y+dy[k]
    if 0 <= mx < n and 0 <= my < n and graph[x][y] < graph[mx][my] :
      dp[x][y] = max(dp[x][y], dfs(mx, my)+1)
  
  return dp[x][y]
    
answer = 0
dp = [[0] * n for _ in range (n)]
for i in range (n) :
  for j in range (n) :
    answer = max(answer, dfs(i,j))

print(answer)