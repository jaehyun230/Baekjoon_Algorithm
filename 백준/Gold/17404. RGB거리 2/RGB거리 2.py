import sys
input = sys.stdin.readline

n = int(input())
#R,G,B 집
house = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
answer = INF
# 색깔별로 수행
for k in range (3) :
  d = [[INF]*n for _ in range(3)]
  for i in range (3) :
    if i == k :
      d[i][0] = house[0][i]
    
  for j in range (1, n) :
    d[0][j] = house[j][0] + min(d[1][j-1], d[2][j-1])
    d[1][j] = house[j][1] + min(d[0][j-1], d[2][j-1])
    d[2][j] = house[j][2] + min(d[0][j-1], d[1][j-1])

  for i in range (3) :
    if i != k :
      answer = min(d[i][n-1], answer)

print(answer)