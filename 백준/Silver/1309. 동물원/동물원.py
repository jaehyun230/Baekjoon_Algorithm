n = int(input())

d = [[0]*3 for _ in range (n)]

#공백 좌 우
d[0][0] = 1
d[0][1] = 1
d[0][2] = 1

for i in range (1, n) :
  d[i][0] = (d[i-1][0] + d[i-1][1] + d[i-1][2])%9901
  d[i][1] = (d[i-1][0] + d[i-1][2])%9901
  d[i][2] = (d[i-1][0] + d[i-1][1])%9901

print(sum(d[n-1])%9901)
