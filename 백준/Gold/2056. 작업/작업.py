import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
for i in range (1, n+1) :
  info = list(map(int, input().split()))
  dp[i] = info[0]
  for j in range(2, len(info)) :
    dp[i] = max(dp[i], dp[info[j]] + info[0])

print(max(dp))