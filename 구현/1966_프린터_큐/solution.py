from collections import deque

n = int(input())

for _ in range (n) :
  a,b = map(int, input().split())
  q = deque()
  data = list(map(int, input().split()))
  count = 0
  for i in data :
    q.append(i)

  while q :
    pri = max(q)
    now = q.popleft()
    if pri == now :
      count +=1
      if b == 0 :
        print(count)
        break
      else :
        b -=1
    else :
      q.append(now)
      if b == 0 :
        b += len(q)-1
      else :
        b -=1
  
