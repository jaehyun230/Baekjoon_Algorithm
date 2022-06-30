from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n+1)

graph = [[] for _ in range (n+1)]
answer = []

for _ in range (m) :
  order = list(map(int, input().split()))
  for i in range (1, len(order)-1) :
    start, end = order[i], order[i+1]
    graph[start].append(end)
    indegree[end] += 1

def topology_sort() :
  q = deque()
  
  for i in range (1, n+1) :
    if indegree[i] == 0 :
      q.append(i)
      

  while q :
    now = q.popleft()
    answer.append(now)
    for i in graph[now] :
      indegree[i] -=1
      if indegree[i] == 0 :
        q.append(i)

topology_sort()

if len(answer) != n :
  print(0)
else :
  for i in answer :
    print(i, end = " ")