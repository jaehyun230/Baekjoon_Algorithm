import heapq

INF = int(1e9)
distance = [INF] * 100001
#찾기시작위치, 검색위치
start, end = map(int, input().split())

distance[start] = 0

q = []

heapq.heappush(q, (0, start))

while q :
  dist, now = heapq.heappop(q)
  if distance[now] < dist :
    continue
  else :
    cost = dist + 1
    if now+1 <= 100000 :
      if cost < distance[now+1] :
        distance[now+1] = cost
        heapq.heappush(q, (cost, now+1))
    if now-1 >= 0 :
      if cost < distance[now-1] :
        distance[now-1] = cost
        heapq.heappush(q, (cost, now-1))
      
    if now*2 <= 100000 :
      if dist < distance[now*2] :
        distance[now*2] = dist
        heapq.heappush(q, (dist, now*2))
    
print(distance[end])
