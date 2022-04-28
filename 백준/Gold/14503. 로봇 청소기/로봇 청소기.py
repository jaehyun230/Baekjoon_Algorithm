import sys
input = sys.stdin.readline
# 맵 세로 가로
n, m = map(int, input().split())
# 로봇 좌표, 방향
x, y, d = map(int, input().split())
# 맵 입력 받기
graph = [list(map(int, input().split())) for _ in range(n)]
# 방문 기록
visitied = [[0] * m for _ in range(n)]
#이동 경우 북/동/남/서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visitied[x][y] = 1
answer = 1

while True :
  
  Flag = False
  for _ in range(4) :
    d = (d+3)%4
    mx = x+dx[d]
    my = y+dy[d]
    if 0<= mx < n and 0<= my < m and graph[mx][my] == 0 and visitied[mx][my] == 0 :
      visitied[mx][my] = 1
      answer +=1
      x, y = mx, my
      Flag = True
      break
      
  if Flag == False :
    mx = x-dx[d]
    my = y-dy[d]
    if 0<= mx < n and 0<= my < m and graph[mx][my] != 1 :
      x = mx
      y = my
    else :
      print(answer)
      break