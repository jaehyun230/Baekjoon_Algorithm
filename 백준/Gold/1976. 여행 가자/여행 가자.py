from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

m = int(input())

graph = [[]*(n+1) for _ in range(n+1)]

for i in range (n) :
  data = list(map(int, input().split()))
  for k in range (n) :
    if data[k] == 1 :
      graph[i+1].append(k+1)
      graph[k+1].append(i+1)

#경로 계획
plan = list(map(int, input().split()))

visited = {}

q = deque()
q.append(plan[0])
visited[plan[0]] = 1

while q :
  x = q.popleft()
  for i in graph[x] :
    if i not in visited :
      visited[i] = 1
      q.append(i)

answer = "YES"

for i in range(m) :
  if plan[i] not in visited :
    answer = "NO"
    break
    
print(answer)