import sys
import math

input = sys.stdin.readline

t = int(input())

def check(x1,y1, x2,y2, cx, cy, r) :
  
  #행성중심부터 시작점까 의 거리
  start = (((x1 - cx) ** 2) + ((y1 - cy) ** 2)) ** 0.5 
  #행성중심부터 도착점까지의 거리
  end = (((x2 - cx) ** 2) + ((y2 - cy) ** 2)) ** 0.5 

  if start < r and end < r :
    return False
  elif start < r :
    return True
  elif end < r :
    return True
    
  return False

for _ in range(t) :
  #시작/ 끝 좌표
  sx, sy, ex, ey = map(int, input().split())
  #행성 정보갯수
  n = int(input())
  planet = [list(map(int, input().split())) for _ in range(n)]

  answer = 0
  for i in planet :
      if check(sx, sy, ex, ey, i[0], i[1], i[2]) :
        answer +=1
        
  print(answer)