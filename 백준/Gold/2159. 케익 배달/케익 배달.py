import sys

input = sys.stdin.readline

n = int(input())

start_x, start_y = map(int, input().split())

q = []
q.append((start_x, start_y, 0))

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]

for _ in range (n) :
  target_x, target_y = map(int, input().split())

  temp = []
     
  for k in range (5) :
    mx = target_x + dx[k]
    my = target_y + dy[k]
    if 0 <= mx < 100001 and 0 <= my < 100001 :
      cost = int(1e12)
      for i in q :
        cost = min(cost, (i[2] + abs(i[0]-mx) + abs(i[1]-my)))        
      temp.append((mx, my, cost))

  q = temp

min_val = int(1e12)

for a,b,c in q :
  min_val = min(min_val, c)
print(min_val)