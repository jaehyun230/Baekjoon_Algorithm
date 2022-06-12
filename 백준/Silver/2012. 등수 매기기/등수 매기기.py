import sys

input = sys.stdin.readline

n = int(input())

num = [int(input()) for _ in range(n)]

num.sort()

answer = 0

for i in range(n) :
  answer +=abs(num[i]-(i+1))

print(answer)