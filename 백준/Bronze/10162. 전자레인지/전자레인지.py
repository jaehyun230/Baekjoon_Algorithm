n = int(input())

num = [[0, 0, 0]]

while n > 0 :
  if n >= 300 :
    n -=300
    num[0][0] += 1
  elif n >= 60 :
    n -=60
    num[0][1] += 1
  else :
    n -=10
    num[0][2] += 1
  
if n == 0 :
  print(num[0][0], num[0][1], num[0][2])
else :
  print(-1)