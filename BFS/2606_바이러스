from collections import deque

#컴퓨터 개수
N = int(input())
# 연결된 network 수
M = int(input())

def BFS(start_n) :
  que = deque()
  que.append(start_n)
  virus_com = []
  virus_com.append(start_n)

  while que :
    which = que.popleft()
    for i in graph[which] :
      if i not in virus_com :
        virus_com.append(i)
        que.append(i)

  print(len(virus_com)-1)
  

graph = [[]*N for _ in range(N+1)]

for _ in range(M) :
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
BFS(1)
