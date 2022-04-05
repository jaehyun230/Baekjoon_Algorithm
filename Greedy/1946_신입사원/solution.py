import sys
input = sys.stdin.readline

#테스트 케이스 수
t = int(input())

for _ in range (t) :
  #지원자 수
  n = int(input())
  score = []
  for i in range (n) :
    a, b = map(int, input().split())
    score.append([a, b])
  score.sort()
  count = 1
  divide_score = score[0][1]

  for i in range(1, n) :
    if divide_score > score[i][1] :
      count +=1
      divide_score = score[i][1]

  print(count)
  
