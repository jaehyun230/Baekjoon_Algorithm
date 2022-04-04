import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range (e) :
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
  
#거쳐야할 지점
p1, p2 = map(int, input().split())

def dijkstra (start) :
  distance = [INF] * (v+1)
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start))
  while q :
    dist, now = heapq.heappop(q)
    if distance[now] < dist :
      continue

    for i in graph[now] :
      cost = dist + i[1]
      if cost < distance[i[0]] :
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  return distance


p1_graph = dijkstra(p1)
p2_graph = dijkstra(p2)

answer = min(p1_graph[1] + p1_graph[p2] + p2_graph[v] , p2_graph[1] + p2_graph[p1] + p1_graph[v])

if answer >= INF :
  print(-1)
else :
  print(answer)
  
