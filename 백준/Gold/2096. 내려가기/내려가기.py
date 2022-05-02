import sys
input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

for _ in range(1) :
  x, y, z = map(int, input().split())
  max_dp[0], max_dp[1], max_dp[2] = x, y, z
  min_dp[0], min_dp[1], min_dp[2] = x, y, z

for i in range (1, n) :
  temp = [0] * 3
  x, y, z = map(int, input().split())
  temp[0] = max(max_dp[0], max_dp[1]) + x
  temp[1] = max(max_dp[0], max_dp[1], max_dp[2]) + y
  temp[2] = max(max_dp[1], max_dp[2]) + z

  for j in range (3) :
    max_dp[j] = temp[j]
  
  temp[0] = min(min_dp[0], min_dp[1]) + x
  temp[1] = min(min_dp[0], min_dp[1], min_dp[2]) + y
  temp[2] = min(min_dp[1], min_dp[2]) + z

  for j in range (3) :
    min_dp[j] = temp[j]

print(max(max_dp), min(min_dp))