import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

dp = [1]*(n+1)

for i in range (n) :
  for j in range(i) :
    if arr[i] > arr[j] :
      dp[i] = max(dp[i], dp[j]+1)


max_dp = (max(dp))
print(max_dp)
idx = dp.index(max_dp)
#가장긴 증가하는 수열
lis = []

while idx >= 0:
    if dp[idx] == max_dp:
        lis.append(arr[idx])
        max_dp -= 1
    idx -= 1

lis = lis[::-1]

for i in lis :
  print(i, end = ' ')