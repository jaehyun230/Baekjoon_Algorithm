import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def topology_sort():
    DP_table = [0] * (n+1)

    q = deque()

    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
            DP_table[i] += times[i]

    while q:
        now = q.popleft()

        for i in graph[now]:
            in_degree[i] -= 1
            DP_table[i] = max(DP_table[i], DP_table[now] + times[i])

            if in_degree[i] == 0:
                q.append(i)


    return DP_table[end]

for _ in range (t) :
  n, k = map(int, input().split())

  times = [0] + list(map(int, input().split()))
  graph = [[] for _ in range (n+1)]
  in_degree = [0] * (n+1)
  
  for i in range (k) :
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1
  
  end = int(input())

  print(topology_sort())

  