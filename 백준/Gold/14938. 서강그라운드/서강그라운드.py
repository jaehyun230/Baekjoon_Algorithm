import heapq
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

item = [0] + list(map(int, input().split()))

graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(r) :
  start, end, cost = map(int, input().split())
  graph[start].append([end, cost])
  graph[end].append([start, cost])

def dijkstra(s) :
  result = 0
  q = []
  heapq.heappush(q, [0, s]) #cost, item수, now위치
  visited = [m+1] * (n+1)
  visited[s] = 0
  
  while q :
    cost, now = heapq.heappop(q)
    for end, val in graph[now] :
      if cost+val < visited[end] :
        visited[end] = cost+val
        heapq.heappush(q, [cost+val, end])

  for i in range(len(visited)) :
    if visited[i] <= m :
      result +=item[i]

  return result

answer = 0
for i in range(1, n+1) :
  answer = max(answer, dijkstra(i))

print(answer)