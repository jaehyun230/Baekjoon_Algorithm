n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

command = list(map(int, input().split()))

#처음에 주사위 모두 면 0
dice = [0, 0, 0, 0, 0, 0]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def turn(num) :
  a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
  #동/ 서/ 북/ 남 순서
  if num == 1 :
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
  elif num == 2 :
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
  elif num == 3 :
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
  elif num == 4 :
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for i in command :
  
  mx = x + dx[i-1]
  my = y + dy[i-1]
  if 0 <= mx < n and 0 <= my < m :
    x, y = mx, my
    turn(i)
    if graph[mx][my] == 0 :
      graph[mx][my] = dice[-1]
    else :
      dice[-1], graph[mx][my] = graph[mx][my], 0

    print(dice[0])