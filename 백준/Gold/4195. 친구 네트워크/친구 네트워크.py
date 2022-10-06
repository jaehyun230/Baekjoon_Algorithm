from collections import defaultdict

import sys

t = int(input())

def union(x, y) :
  x = find(x)
  y = find(y)

  if x == y :
    return

  else :
    dic[y] = x
    visited[x] += visited[y]

def find(target) :
  if target == dic[target] :
    return target
  else :
    dic[target] = find(dic[target])
    return dic[target]

for _ in range(t) :
  n = int(input())
  dic = defaultdict(str)
  visited = defaultdict(int)
  
  for _ in range(n) :
    result = set()
    a, b = input().split()

    if a not in dic :
      dic[a] = a
      visited[a] = 1
    if b not in dic :
      dic[b] = b
      visited[b] = 1
    
    union(a, b)
    print(visited[find(a)])