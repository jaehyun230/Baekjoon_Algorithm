import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

def dfs(a, c) :
  global max_dist
  global max_dst
  answer = c
  
  for i in graph[a] :
    dst, cost = i[0], i[1]
    
    if visit[dst] == 0 :
      visit[dst] = 1
      dfs(dst, answer+cost)
      if max_dist <= answer+cost :
        max_dist = answer+cost
        max_dst = dst
  
graph = [[] for _ in range(n+1)]

for _ in range (1, n) :
  x, y, z = map(int, input().split())
  graph[x].append([y, z])
  graph[y].append([x, z])


max_dist = 0
max_dst = 1
visit = [0] * (n+1)
visit[1] = 1
dfs(1,0)

visit = [0] * (n+1)
visit[max_dst] = 1
dfs(max_dst, 0)

print(max_dist)
