import sys

input = sys.stdin.readline

n = int(input())

lope = [list(map(int, input().split())) for _ in range (n)]

lope.sort()

dp = [1] * n

for i in range (n) :
  for j in range (i) :
    if lope[i][1] > lope[j][1] and dp[i] < dp[j] + 1 :
      dp[i] = dp[j] + 1

print(n-max(dp))
