from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range (n+1)]

cost = [0] * (n+1)
need = [[0] * (n+1) for _ in range (n+1)]
indegree = [0] * (n+1)

for _ in range(m) :
  #x만드는데 y가 k개 필요
  x, y, k = map(int, input().split())
  graph[y].append((x, k))
  indegree[x] +=1

def topology_sort() :
  q = deque()
  for i in range (1, n+1) :
    if indegree[i] == 0 :
      q.append(i)

  while q :
    now = q.popleft()
    #now 로 a 만드는데 b개 필요
    for a,b in graph[now] :
      if need[now].count(0) == n + 1 :
        need[a][now] += b
      else :
        for i in range(1, n + 1):
          need[a][i] += need[now][i] * b

      indegree[a] -=1
      if indegree[a] == 0 :
        q.append(a)
      
topology_sort()

for i in range(1, n+1) :
  if need[n][i] > 0 :
    print(i, need[n][i])