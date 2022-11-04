import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

total = 0

start, end = 0, 0

INF = int(1e9)
answer = INF

while True :
  if total >= m :
    answer = min(answer, end - start)
    total -= arr[start]
    start +=1
  elif end == n :
    break
  else :
    total += arr[end]
    end +=1

if answer == INF :
  print(0)
else :
  print(answer)