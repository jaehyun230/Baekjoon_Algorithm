from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

def bfs(graph, start):
  queue = deque()
  queue.append(start)
  if visited[start] == 0:
    # 이분 1, 2로 하고 방문하지 않은곳은 0으로 표시
    visited[start] = 1  
  while queue:
    v = queue.popleft()
    color = visited[v]
    for i in graph[v]:  
      if visited[i] == 0:  
        queue.append(i)
        if color == 1: 
          visited[i] = 2
        else:
          visited[i] = 1
      elif visited[i] == 1:
        if color == 1:
            print("NO")
            return False
      elif visited[i] == 2:
        if color == 2:
          print("NO")
          return False
  return True
    
for _ in range (t) :
  v, e = map(int, input().split())
  graph = [[] for _ in range (v+1)]
  visited = [0] * (v+1)
  for i in range (e) :
    a, b  = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  answer = 0
  for i in range (1, v+1) :
    if not bfs(graph, i) :
      answer = 1
      break
  if answer == 0 :
    print("YES")