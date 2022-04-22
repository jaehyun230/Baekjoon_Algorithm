from collections import deque
import sys

input = sys.stdin.readline

#테스트 케이스 수
t = int(input())

#맥주 50m*20 이동 가능
can_move = 1000

answer = []

def bfs(start, end, store) :
  q = deque()
  q.append((start[0], start[1]))

  while q :
    x, y = q.popleft()
    if abs(x-end[0]) + abs(y-end[1]) <= can_move :
      return True
    else :
      for i in range(n) :
        if abs(x-store[i][0]) + abs(y-store[i][1]) <= 1000 and visited[i] == False:
          visited[i] = True
          q.append((store[i][0], store[i][1]))
          
  return False
  

for _ in range(t) :
  #맥주 편의점 개수
  n = int(input())
  #출발 지점
  start = list(map(int, input().split()))
  #편의점
  store = []
  visited = [False] * n
  for _ in range (n) :
    x, y = map(int, input().split())
    store.append((x,y))
    #도착 지점

  end = list(map(int, input().split()))
  if bfs(start, end, store) :
    answer.append("happy")
  else :
    answer.append("sad")

for i in answer :
  print(i)