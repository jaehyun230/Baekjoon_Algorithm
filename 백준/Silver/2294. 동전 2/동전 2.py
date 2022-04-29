n, k = map(int, input().split())

coin = []
INF = int(1e9)
dp = [INF] * (100001)

for _ in range(n) :
  number = int(input())
  coin.append(number)
  dp[number] = 1

coin = list(set(coin))

for i in range(k+1) :
  for j in coin :
    if i-j >= 0 :
      dp[i] = min(dp[i], dp[i-j]+1)

if dp[k] == INF :
  print(-1)
else :
  print(dp[k])