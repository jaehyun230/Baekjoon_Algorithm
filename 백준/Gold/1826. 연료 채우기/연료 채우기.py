import heapq
import sys

input = sys.stdin.readline
# 주유소 갯수
n = int(input())
# 주유소 모음
oils = []
# 주유소 입력
for _ in range (n) :
  x, y = map(int, input().split())
  heapq.heappush(oils, (x, -y))

#골지점 거리 , 현재 기름양
goal, oil = map(int, input().split())
#채운 횟수
answer = 0
#갈수있는 주유소 모음
move = []
while oil < goal :
  # 방문 가능한 주유소들 가져오기
  while oils and oils[0][0] <=  oil :
    pos, plus_oil = heapq.heappop(oils)
    heapq.heappush(move, (plus_oil, pos))
     
  if not move :
    answer = -1
    break
    
  max_oil, oil_pos = heapq.heappop(move)
  oil += max_oil * -1
  answer +=1

print(answer)