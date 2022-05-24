S = list(input())
T = list(input())

flag = False
while T :
  if S == T :
    flag = True
    break
  elif T[-1] == 'B' :
    T.pop()
    T.reverse()
  elif T[-1] == 'A' :
    T.pop()

if flag :
  print(1)
else :
  print(0)