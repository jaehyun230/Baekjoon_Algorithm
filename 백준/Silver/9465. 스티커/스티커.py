t = int(input())

for _ in range (t) :
  n = int(input())
  score = []
  for _ in range(2) :
    score.append(list(map(int, input().split())))

  d = [[0] * (n) for _ in range(2)]
  
  d[0][0] = score[0][0]
  d[1][0] = score[1][0]
  if n >= 2 :
    d[0][1] = d[1][0] + score[0][1]
    d[1][1] = d[0][0] + score[1][1]
  
  for i in range(2,n) :
    d[0][i] = max(d[1][i-1] +score[0][i], d[1][i-2] + score[0][i])
    d[1][i] = max(d[0][i-1] +score[1][i], d[0][i-2] + score[1][i])
  print(max(d[0][n-1], d[1][n-1]))