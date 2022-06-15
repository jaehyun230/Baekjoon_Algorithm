import sys

input = sys.stdin.readline

n, k = map(int, input().split())

bag = [list(map(int, input().split())) for _ in range (n)]

dp = [[0] * (k+1) for _ in range (n)]

for i in range (n) :
  for j in range (k+1) :
    weight = bag[i][0]
    value = bag[i][1]

    if j < weight :
      dp[i][j] = dp[i-1][j]

    else :
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n-1][k])