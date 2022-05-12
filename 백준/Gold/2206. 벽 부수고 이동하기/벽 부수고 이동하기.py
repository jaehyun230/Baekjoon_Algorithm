from collections import deque
import sys

input = sys.stdin.readline
# 맵 크기
n, m = map(int, input().split())
# 맵
graph = []
# 이동방향
dx =[-1, 1, 0, 0]
dy =[0, 0, -1, 1]

INF = int(1e9)
answer = INF

# bfs 탐색
def bfs() :
  visited = [[[0] * 2 for _ in range(m)] for _ in range (n)]
  # 벽을 부술수있는 상태에서 시작 [1] 이 부술수있는 상태로 진행 [0]은 한번 부순상태
  visited[0][0][1] = 1
  q = deque()
  q.append((0, 0, 1))
  
  while q :
    now_x, now_y, state = q.popleft()
    if now_x == n-1 and now_y == m-1 :
      return visited[now_x][now_y][state]
    for i in range(4) :
      mx = now_x + dx[i]
      my = now_y + dy[i]
      if 0 <= mx < n and 0 <= my < m :
        if graph[mx][my] == 1 and state == 1 :
          visited[mx][my][0] = visited[now_x][now_y][state] + 1
          q.append((mx, my, 0))
        elif graph[mx][my] == 0 and visited[mx][my][state] == 0 :
          visited[mx][my][state] = visited[now_x][now_y][state] + 1
          q.append((mx, my, state))
      
  # 도달 불가능 할 경우
  return -1
  
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

print(bfs())