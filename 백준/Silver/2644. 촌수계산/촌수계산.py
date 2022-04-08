from collections import deque

n = int(input())
start, end = map(int, input().split())
edge = int(input())

graph = []
distance = [0] * (n+1)
#print(family)

for _ in range (edge) :
  a,b = map(int, input().split())
  graph.append((a, b))
  graph.append((b, a))

def bfs(start, graph) :
  q = deque()
  q.append((0, start))
  while q :
    dist, now = q.popleft()
    for i in graph :
      if now == i[0] and distance[i[1]] == 0 :
        cost = dist + 1
        distance[i[1]] = cost
        q.append((cost, i[1]))

bfs(start, graph)
if distance[end] == 0 :
  print(-1)
else :
  print(distance[end])
    