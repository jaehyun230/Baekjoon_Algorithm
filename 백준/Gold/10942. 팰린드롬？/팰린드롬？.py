import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

m = int(input())

dp = [[0] * n for _ in range(n)]

for length in range(n):
    for start in range(n - length):
        end = start + length
        
        # 글자수 1개
        if start == end:
            dp[start][end] = 1
        # 시작점의 글자와 끝점의 글자가 같은경우
        elif arr[start] == arr[end]:
        	# 두 글자 팰린드롬
            if start + 1 == end : 
              dp[start][end] = 1
            # 가운데 문자열이 팰린드롬이라면 팰린드롬
            elif dp[start+1][end-1] == 1 : 
              dp[start][end] = 1

for _ in range(m) :
  start, end = map(int, input().split())
  print(dp[start-1][end-1])