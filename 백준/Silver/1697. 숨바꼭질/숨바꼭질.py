from collections import deque

n, m = map(int, input().split())

INF = int(1e9)

dist = [INF] * 100001

def bfs(start, end) :
  q = deque()
  q.append((start, 0))
  
  while q :
    now, cost = q.popleft()
    if now == end :
      return cost
    else :
      if now*2 <= 100000 and dist[now*2] > cost+1 :
        q.append((now*2, cost+1))
        dist[now*2] = cost + 1
      if now+1 < 100000 and dist[now+1] > cost+1 :
        q.append((now+1, cost+1))
        dist[now+1] = cost + 1
        
      if now-1 >= 0 and dist[now-1] > cost+1 :
        q.append((now-1, cost+1))
        dist[now-1] = cost + 1
      
print(bfs(n, m))