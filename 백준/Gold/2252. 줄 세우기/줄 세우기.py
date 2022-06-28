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
  q = deque()
  for k in range (1, n+1) :
    if indegree[k] == 0 :
      q.append(k)

  while q :
    now = q.popleft()
    for i in graph[now] :
      indegree[i] -=1
      if indegree[i] == 0 :
        q.append(i)
    print(now, end = " ")

topology_sort()