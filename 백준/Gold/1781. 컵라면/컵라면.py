import sys
import heapq

input = sys.stdin.readline

#데드라인 n이하 자연수, n개의 입력
n = int(input())

problem = []

for _ in range(n) :
  #데드라인, 컵라면 수
  x,y = map(int, input().split())
  problem.append((x, y))
  
problem.sort()

q = []

for d_day, score in problem :
  heapq.heappush(q, score)
  if d_day < len(q) :
    heapq.heappop(q)
  

print(sum(q))