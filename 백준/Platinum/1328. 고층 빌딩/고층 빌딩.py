# 총 수, 왼쪽에서 본 수 , 오른쪽에서 본 수
n, l, r = map(int, input().split())

dp = [[[0 for i in range(101)] for j in range(101)] for k in range(101)]

dp[1][1][1] = 1

for i in range (2, 101) :
  for j in range(1, 101) :
    for k in range(1, 101) :
      dp[i][j][k] = (dp[i-1][j][k-1] + dp[i-1][j-1][k] + dp[i-1][j][k] * (i-2)) % 1000000007

print(dp[n][l][r])