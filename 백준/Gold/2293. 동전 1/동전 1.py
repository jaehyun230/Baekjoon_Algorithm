n, k = map(int, input().split())

coin = []

dp = [0] * (k+1)
dp[0] = 1
for _ in range(n) :
  number = int(input())
  coin.append(number)

for i in coin :
  for j in range(i, k+1) :
    if j-i >= 0 :
      dp[j] += dp[j-i]

print(dp[k])