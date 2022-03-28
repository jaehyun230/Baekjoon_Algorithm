N = 1000 - int(input())
Count = 0

while N > 0 :
  if N >=500 :
    N -=500
  elif N>=100 :
    N -=100
  elif N>=50 :
    N -=50
  elif N>=10 :
    N -=10
  elif N>=5 :
    N -=5
  else :
    N -=1
  Count +=1

if N < 0 :
  print(-1)
else :
  print(Count)
