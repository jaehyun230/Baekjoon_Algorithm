from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())


indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
q = deque()

for _ in range(m) :
  x, y = map(int, input().split())
  graph[x].append(y)
  indegree[y] +=1

for i in range(1, n+1) :
  if indegree[i] == 0 :
    q.append(i)

while q :
  student = q.popleft()

  for i in graph[student] :
    indegree[i] -=1
    if indegree[i] == 0 :
      q.append(i)
  print(student, end=" ")