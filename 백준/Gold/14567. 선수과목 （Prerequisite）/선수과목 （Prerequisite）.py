from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range (n+1)]


for _ in range (m) :
  start, end = map(int, input().split())
  indegree[end] +=1
  graph[start].append(end)

def topology_sort() :
  time = [0] * (n+1)
  q = deque()
  for i in range (1, n+1) :
    if indegree[i] == 0 :
      q.append((i, 1))
      time[i] = 1

  while q :
    now, c = q.popleft()
    for i in graph[now] :
      indegree[i] -= 1
      if indegree[i] == 0 :
        q.append((i, c+1))
        time[i] = max(time[i], c+1)
  return time

sol = topology_sort()
for i in range(1, n+1) :
  print(sol[i], end=" ")