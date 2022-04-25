import sys

input = sys.stdin.readline

n = int(input())

graph = []

for _ in range (n) :
  graph.append(list(map(int, input().split())))

#오른쪽 모양 -
shape_r = [[0]*n for _ in range (n)]
#대각선 모양 \
shape_c = [[0]*n for _ in range (n)]
#내려가는 모양 |
shape_d = [[0]*n for _ in range (n)]

shape_r[0][1] = 1

for i in range (n) :
  for j in range (2, n) :
    if graph[i][j] == 0 :
      shape_r[i][j] = shape_r[i][j-1] + shape_c[i][j-1]
    if graph[i][j] == 0 :
      shape_d[i][j] = shape_d[i-1][j] + shape_c[i-1][j]
    if graph[i][j] == 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0 :
      if i-1 >= 0 :
        shape_c[i][j] = shape_c[i-1][j-1] + shape_r[i-1][j-1] + shape_d[i-1][j-1]

print(shape_r[n-1][n-1]+shape_c[n-1][n-1]+shape_d[n-1][n-1])