from collections import deque

n = int(input())
INF = int(1e9)

# 방문체크
dist = [[INF]* (n+1) for _ in range(n+1)]

q = deque()
# 화면 수, 클립보드 수
q.append((1,0))  

dist[1][0] = 0

while q:
    s,c = q.popleft()
    if dist[s][s] == INF: 
        dist[s][s] = dist[s][c] + 1
        q.append((s,s))
    if s+c <= n and dist[s+c][c] == INF:
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and dist[s-1][c] == INF:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))

print(min(dist[n]))