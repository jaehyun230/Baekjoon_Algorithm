from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for i in range (1, t+1) :
  k, m, p = map(int, input().split())
  indegree = [[0]* 3 for _ in range (m+1)]
  graph = [[] for _ in range (m+1)]
  for _ in range (p) :
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b][0] += 1

  q = deque()

  for s in range(1, m+1) :
    if indegree[s][0] == 0 :
      q.append(s)
      indegree[s][1] = 1  

  while q :
    now = q.popleft()
    for x in graph[now] :
      indegree[x][0] -=1
      if indegree[x][1] < indegree[now][1] :
        indegree[x][1] = indegree[now][1]
        indegree[x][2] = 1
      elif indegree[x][1] == indegree[now][1] :
        indegree[x][2] +=1
      if indegree[x][0] == 0 :
        if indegree[x][2] > 1 :
          indegree[x][1] +=1
        q.append(x)

  print(i, indegree[m][1])