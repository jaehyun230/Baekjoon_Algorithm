import sys

n = int(input())

for _ in range (n) :
  count = 0
  data = sys.stdin.readline().rstrip()
  data = list(data)
  for i in data :
    if i == '(' :
      count +=1
    elif i == ')' :
      count -=1
      if count < 0 :
        break
      
  if count == 0 :
    print("YES")
  else :
    print("NO")