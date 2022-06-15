n = int(input())

num = list(map(int, input().split()))

answer = 0

dp = [0] * (n+1)

for i in range (1, n+1) :
  for j in range (1, i+1) :
    dp[i] = max(dp[i], dp[i-j] + num[j-1])

print(dp[n])