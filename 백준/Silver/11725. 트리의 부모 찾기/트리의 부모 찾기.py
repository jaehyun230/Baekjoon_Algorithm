from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range (n-1) :
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

answer = [-1] * (n+1)

q = deque()
q.append(1)

while q :
  now = q.popleft()
  for i in graph[now] :
    if visited[i] == 0 :
      visited[i] = 1
      answer[i] = now
      q.append(i)

for i in range(2, n+1) :
  print(answer[i])