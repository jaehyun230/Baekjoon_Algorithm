n = int(input())
#최대 점수
score = [0]*301
#해당 계단 점수
stairs = [0]
for i in range (n) :
  stairs.append(int(input()))

if n == 1:
  print(stairs[1])
  
elif n == 2:
  print(stairs[1]+stairs[2])
  
else :
  score[1] = stairs[1]
  score[2] = stairs[1]+stairs[2]
  score[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])

  for i in range (4, n+1) :
    score[i] = max(score[i-3]+stairs[i-1]+stairs[i], score[i-2]+stairs[i])

  print(score[n])

