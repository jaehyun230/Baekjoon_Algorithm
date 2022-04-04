import heapq
# sys의 사용 여부로 시간초과가 날수도있음 참고
import sys
input = sys.stdin.readline

# 버스의 개수
n = int(input())
# 버스 간선 개수
m = int(input())

INF = int(1e9)

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for i in range(m) :
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

start, end = map(int, input().split())

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

print(distance[end])
