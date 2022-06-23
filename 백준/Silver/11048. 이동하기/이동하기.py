import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range (n)]

dp = [[0]*m for _ in range (n)]

dx = [1,1,0]
dy = [0,1,1]

answer = 0
for i in range(n) :
  for j in range(m) :
    for k in range(3) :
      mx = i+dx[k]
      my = j+dy[k]
      if 0<= mx < n and 0 <= my < m :
        dp[mx][my] = max(dp[mx][my], dp[i][j] + graph[mx][my])

print(dp[n-1][m-1]+graph[0][0])