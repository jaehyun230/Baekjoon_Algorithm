from collections import deque
import sys

input = sys.stdin. readline

n, m = map(int, input().split())

graph = [list(input().rstrip()) for _ in range (n)]

for i in range(n) :
  for j in range(m) :
    if graph[i][j] == 'R' :
      rx, ry = i, j
    elif graph[i][j] == 'B' :
      bx, by = i, j
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by) :
  q = deque()
  q.append((rx, ry, bx, by))
  #방문체크 중복제거
  visited = []
  visited.append((rx, ry, bx, by))

  count = 0
  while q :
    for _ in range (len(q)) :
      rx, ry, bx, by = q.popleft()
      if count > 10 :
        count = -1
        return -1
      if graph[rx][ry] == 'O' :
        return count

      for i in range(4) :
        mrx, mry, mbx, mby = rx, ry, bx, by
      
        while True :
          mrx = mrx+dx[i]
          mry = mry+dy[i]

          if graph[mrx][mry] == '#' :
            mrx -=dx[i]
            mry -=dy[i]
            break
          if graph[mrx][mry] == 'O' :
            break
          
        while True :
          mbx = mbx+dx[i]
          mby = mby+dy[i]

          if graph[mbx][mby] == '#' :
            mbx -=dx[i]
            mby -=dy[i]
            break
          if graph[mbx][mby] == 'O' :
            break

        if graph[mbx][mby] == 'O' :
          continue
        # 두 구슬의 위치 같은 경우
        if mrx == mbx and mry == mby: 
          if abs(mrx - rx) + abs(mry - ry) > abs(mbx - bx) + abs(mby - by): 
            mrx -= dx[i]
            mry -= dy[i]
          else:
            mbx -= dx[i]
            mby -= dy[i]
        #해당위치 가져본적 없다면
        if (mrx, mry, mbx, mby) not in visited :
          q.append((mrx, mry, mbx, mby))
          visited.append(((mrx, mry, mbx, mby)))
    
    count +=1
  return -1

print(bfs(rx, ry, bx, by))