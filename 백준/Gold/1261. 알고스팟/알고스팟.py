import heapq
import sys

input = sys.stdin.readline

m, n = map(int, input().split())

graph = [ list(map(int, input().rstrip())) for _ in range(n)]
INF = int(1e9)
visited = [[INF] * m for _ in range (n)]

q = []
heapq.heappush(q, (0, 0, 0))
visited[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q :
  cost, x, y = heapq.heappop(q)
  if x == n-1 and y == m-1 :
    print(cost)
    break
  for i in range(4) :
    mx = x+dx[i]
    my = y+dy[i]
    if 0 <= mx < n and 0 <= my < m :  
      if graph[mx][my] == 0 and visited[mx][my] > cost :    
        visited[mx][my] = cost
        heapq.heappush(q, (cost, mx, my))
      if graph[mx][my] == 1 and visited[mx][my] > cost+1 :
        visited[mx][my] = cost+1
        heapq.heappush(q, (cost+1, mx, my))
