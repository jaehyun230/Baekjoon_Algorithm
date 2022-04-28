n = int(input())

top = list(map(int, input().split()))

#시작 부분
receive = []
index = []
answer = []

for i in range (len(top)) :
  while True :
    if not receive :
      receive.append(top[i])
      index.append(i)
      answer.append(0)
      break
    elif receive[-1] <= top[i] :
      receive.pop()
      index.pop()
    
    else :
      answer.append(index[-1]+1)
      receive.append(top[i])
      index.append(i)
      break

for i in answer :
  print(i, end=" ")