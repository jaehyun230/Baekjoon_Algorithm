import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = input().rstrip()

eated = [0] * (n+1)

answer = 0
for i in range (n) :
  if arr[i] == 'P' :
    start = i - k
    end = i + k
    if start < 0 :
      start = 0
    if end >= n :
      end = n-1
    for j in range (start, end+1) :
      if eated[j] == 0 and arr[j] == 'H' :
        eated[j] = 1
        answer +=1
        break

print(answer)