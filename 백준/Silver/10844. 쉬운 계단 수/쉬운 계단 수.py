n = int(input())

dp = [[0] * (10) for _ in range(101)]

#dp[i][j] i는 계단수, j는 마지막 계단 번호
for i in range(1, 10) :
  dp[1][i] = 1

for i in range(2,101) :
  for j in range(10) :

    if j == 0 :
      dp[i][j] = dp[i-1][j+1] %1000000000
    elif j == 9 :
      dp[i][j] = dp[i-1][j-1] %1000000000
    else :
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] %1000000000

print(sum(dp[n])%1000000000)