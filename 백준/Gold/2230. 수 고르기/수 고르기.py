import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num = [int(input()) for _ in range(n)]

num.sort()

front = 0
back = 0

answer = 2 * (10**9)

while front < n :

  if num[front] - num[back] == m :
    answer = m
    break

  if num[front] - num[back] > m :
    answer = min(answer, num[front] - num[back])
    back +=1

  else :
    front +=1

print(answer)