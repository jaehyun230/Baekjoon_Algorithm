from collections import deque

f, s, g, u, d = map(int, input().split())

def bfs(start, goal) :
  q = deque()
  q.append((start, 0))
  visited = [0] * (f+1)
  visited[start] = 1

  while q :
    now, cost = q.popleft()
    if now == goal :
      return cost
    else :
      if now+u <= f and visited[now+u] == 0 :
        q.append((now+u, cost+1))
        visited[now+u] = 1
      if now-d > 0 and visited[now-d] == 0 :
        q.append((now-d, cost+1))
        visited[now-d] = 1
        
  return -1

result = bfs(s, g)
if result >= 0 :
  print(result)
else :
  print("use the stairs")