from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
indegree = [0] * (n+1)
cost = [0] * (n+1)
build = [[] for _ in range (n+1)]
for i in range (1, n+1) :
  data = list(map(int, input().split()))
  cost[i] = data[0]
  for k in range (1, len(data)) :
    if data[k] == -1 :
      break
    indegree[i] +=1
    build[data[k]].append(i)

def topology_sort() :
  dp = [0] * (n+1)
  q = deque()

  for i in range(1, n+1) :
    if indegree[i] == 0 :
      q.append(i)

  while q :
    #현재 건설할것
    now = q.popleft()
    dp[now] += cost[now]
    for k in build[now] :
      indegree[k] -=1
      dp[k] = max(dp[k], dp[now])
      if indegree[k] == 0 :
        q.append(k)
        
  return dp

answer = topology_sort()

for i in range (1, n+1) :
  print(answer[i])