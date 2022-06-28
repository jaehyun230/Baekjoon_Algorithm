import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n+1)
problem = [[] for _ in range (n+1)]

for _ in range (m) :
  #먼저풀면 좋은것, 나중풀것
  start, end = map(int, input().split())
  indegree[end] +=1
  problem[start].append(end)

def topology_sort() :
  q = []
  answer = []
  for i in range (1, n+1) :
    if indegree[i] == 0 :
      heapq.heappush(q, i)
      
  while q :
    now = heapq.heappop(q)
    answer.append(now)
    for k in problem[now] :
      indegree[k] -=1
      if indegree[k] == 0 :
        heapq.heappush(q, k)
        
  return answer

sol = topology_sort()
for i in sol :
  print(i, end = " ")