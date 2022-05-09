n = int(input())

child = [int(input()) for _ in range(n)]

dp = [0] * (n+1)

#가장 긴 수열 이용
for i in range(n) :
  dp[i] = 1
  for j in range(i) :
    if child[j] < child[i] :
      dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))