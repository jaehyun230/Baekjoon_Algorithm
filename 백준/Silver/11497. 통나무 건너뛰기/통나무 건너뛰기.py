import sys

input = sys.stdin.readline

#테스트 케이스 수
t = int(input())

for _ in range (t) :
  n = int(input())
  wood = list(map(int, input().split()))
  wood.sort()
  dp = [0] * len(wood)
  for i in range (len(wood)) :
    if i%2 == 0 :
      dp[i//2] = wood[i]
    else :
      dp[-(i//2+1)] = wood[i]

  answer = 0
  for i in range(len(dp)-1) :
    answer = max(answer, abs(dp[i]-dp[i+1]))
  print(answer)
  