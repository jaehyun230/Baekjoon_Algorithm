import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range (n)]

tar_graph = [list(map(int, input().rstrip())) for _ in range (n)]

count = 0
flag = True

def convert(x,y) :
  for i in range(x, x+3) :
    for j in range(y, y+3) :
      graph[i][j] = 1 - graph[i][j]

for i in range (n-2) :
  for j in range (m-2) :
    if graph[i][j] != tar_graph[i][j] :
      convert(i, j)
      count +=1

for i in range (n) :
  for j in range (m) :
    if graph[i][j] != tar_graph[i][j] :
      flag = False

if flag :
  print(count)
else :
  print(-1)