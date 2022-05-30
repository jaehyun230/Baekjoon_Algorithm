import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range (k) :
  start, end, cost = map(int, input().split())
  if cost > graph[start][end] :
    graph[start][end] = cost


dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(2, n+1) :
  dp[i][2] = graph[1][i]

for i in range(2, n+1):
    for j in range(3, m+1):
        for l in range(1, i):
            if graph[l][i] and dp[l][j-1]:
                dp[i][j]=max(dp[l][j-1]+graph[l][i], dp[i][j])
    
print(max(dp[n]))