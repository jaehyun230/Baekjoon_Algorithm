from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range (n) :
  x = int(input())
  if x != 0 :
    queue.append(x)
  else :
    queue.pop()

print(sum(queue))
