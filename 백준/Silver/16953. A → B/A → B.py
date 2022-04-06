from collections import deque

start, end = map(int, input().split())

q = deque()
q.append((1, start))

INF = int(1e9)
count = [INF]
while q :
  cost, now = q.popleft()
  if now == end :
    count.append(cost)
  if now * 2 <= end :
    q.append((cost+1, now*2))
  if (now*10) + 1 <= end :
    q.append((cost+1, now*10+1))

if min(count) == INF :
  print(-1)
else :
  print(min(count))