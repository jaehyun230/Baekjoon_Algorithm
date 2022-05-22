import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range (t) :
  n, m = map(int, input().split())
  q = []
  for _ in range(m) :
    x,y = map(int, input().split())
    heapq.heappush(q, ((y, x)))

  answer = 0
  dic = {}
  while q :
    end, start = heapq.heappop(q)
    if end > n :
      end = n
    for i in range (start, end+1) :
      if i not in dic :
        dic[i] = 1
        answer +=1
        break
        
  print(answer)