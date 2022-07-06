import sys
import math

input = sys.stdin.readline

#웅덩이 갯수, 널빤지 길이
n, l = map(int, input().split())

pool = [list(map(int, input().split())) for _ in range (n)]

pool.sort()

now = pool[0][0]
answer = 0
for i in range (n) :
  start, end = pool[i][0], pool[i][1]
  if now >= end :
    continue
  elif start >= now :
    need = math.ceil((end - start)/l)
    now = start + need*l
    answer += need
  else :
    need = math.ceil((end - now)/l)
    now = now + need*l
    answer += need
    
print(answer)