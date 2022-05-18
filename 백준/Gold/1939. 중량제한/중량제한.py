from collections import deque
import sys

input = sys.stdin.readline
#섬, 다리정보 갯수
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

def bfs(value) :
  visited = [0 for _ in range (n+1)]
  visited[start] = 1
  q = deque()
  q.append(start)
  while q :
    now = q.popleft()
    if now == end :
      return True
    for i in graph[now] :
      if value <= i[1] and visited[i[0]] == 0 :
        q.append(i[0])
        visited[i[0]] = 1
  return False
  
for _ in range (m) :
  x, y, z = map(int, input().split())
  #양방향
  graph[x].append((y,z))
  graph[y].append((x,z))
  
#시작점과 도착점
start, end = map(int, input().split())

low , high = 1, 1000000000

while low <= high :
  mid = (low + high)//2
  if bfs(mid) :
    low = mid + 1
  else :
    high = mid - 1

print(high)