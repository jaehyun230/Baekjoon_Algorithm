from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
problem_num = 0
while True :
  n = int(input())
  if n == 0 :
    break

  problem_num +=1
  
  graph = [ list(map(int, input().split())) for _ in range(n)]
  INF = int(1e9)
  cost = [[INF] * n for _ in range(n)]
  q = deque()
  # 시작부분
  q.append((0, 0, graph[0][0]))
  cost[0][0] = graph[0][0]
  while q :
    x, y, c = q.popleft()
    
    for i in range (4) :
      mx = x+dx[i]
      my = y+dy[i]

      if 0 <= mx < n and 0 <= my < n and c+graph[mx][my] < cost[mx][my] :
        cost[mx][my] = c+graph[mx][my]
        q.append((mx, my, c+graph[mx][my]))

  print(f'Problem {problem_num}: {cost[n-1][n-1]}')