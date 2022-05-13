import heapq
import sys

input = sys.stdin.readline

n = int(input())

pos = []
nag = []

#가장 작은 절대값 찾기
def search() :
  #두칸다 비었을 경우
  if not pos and not nag :
    return 0

  val_1 , val_2 = int(1e9), int(1e9)
  if pos :
    val_1 = heapq.heappop(pos) 
  if nag :
    val_2 = heapq.heappop(nag)

  if val_1 == int(1e9) and val_2 == int(1e9) :
    return 0
  elif val_1 >= val_2 :
    heapq.heappush(pos, val_1 )
    return val_2 * -1
  else :
    heapq.heappush(nag, val_2)
    return val_1
    
for _ in range(n) :
  x = int(input())
  if x < 0 :
    heapq.heappush(nag, -x)
  elif x == 0 :
    print(search())
  elif x > 0 :
    heapq.heappush(pos, x)