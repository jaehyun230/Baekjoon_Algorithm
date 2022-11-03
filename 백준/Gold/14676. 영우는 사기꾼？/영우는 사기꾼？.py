from collections import defaultdict
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

graph = [[]* (n+1) for _ in range(n+1)]
indegree = [0] * (n+1)

build = defaultdict(int)

for _ in range(m) :
  start, end = map(int, input().split())
  indegree[end] +=1
  graph[start].append(end)


def can_build(num) :
  if indegree[num] == 0 :
    return True
  else :
    return False

def check(command, num) :
  if command == 1 :
    if can_build(num) :
      build[num] +=1
      if build[num] == 1 :
        for i in graph[num] :
          indegree[i] -=1
      return True
    else :
      return False
  else :
    if build[num] > 0 :
      build[num] -=1
      if build[num] == 0 :
        for i in graph[num] :
          indegree[i] +=1
      return True
    else :
      return False
    
answer = True

for _ in range(k) :
  command, num = map(int, input().split())
  flag = check(command, num)
  if flag == False :
    answer = False

if answer :
  print("King-God-Emperor")
else :
  print("Lier!")