import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1  
dp[2] = 2

for i in range (3, n+1) :
  dp[i] = dp[i-1] + dp[i-2]

seat = []
for _ in range (m) :
  seat.append(int(input()))

answer = 1
cursor = 0
for i in range (m+1) :
  if i == m :
    answer *= dp[n-cursor]
  else :
    answer *= dp[seat[i]-cursor-1]
    cursor = seat[i]
  
print(answer)