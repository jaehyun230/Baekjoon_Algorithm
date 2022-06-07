import sys

input = sys.stdin.readline

n = int(input())

answer = [-1] * n

num = list(map(int, input().split()))

stack = []

for i in range(n) :
  while stack and stack[-1][0] < num[i] :
    tmp, idx = stack.pop()
    answer[idx] = num[i]
  stack.append((num[i], i))

for i in answer :
  print(i, end =" ")