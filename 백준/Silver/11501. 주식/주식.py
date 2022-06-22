import sys

input = sys.stdin.readline

t = int(input())

for _ in range (t) :
  n = int(input())

  stock = list(map(int,input().split()))

  max_val = stock[-1]  
  now_val = 0
  answer = 0
  for i in range (1, n+1) :
    if max_val < stock[-i] :
      max_val = stock[-i]
    else :
      answer += max_val - stock[-i]
  print(answer)