import sys

input = sys.stdin.readline

n, m = map(int, input().split())

use = [0] + list(map(int, input().split()))

c = [0] + list(map(int, input().split()))
result = sum(c)

dp = [[0 for _ in range(sum(c)+1)] for _ in range(n+1)]

for i in range (1, n+1) :
  byte = use[i]
  cost = c[i]
  
  for j in range (1, sum(c)+1) :
    if j < cost :
      dp[i][j] = dp[i-1][j]
    else :
      dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])

    if dp[i][j] >= m :
      result = min(result, j)

if m !=0 :
  print(result)
else :
  print(0)