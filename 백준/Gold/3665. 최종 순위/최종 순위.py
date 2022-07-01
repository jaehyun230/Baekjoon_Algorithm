from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    # 작년 순위
    n = int(input())
    rank = list(map(int,input().split()))
    cntLink = [-1] + [0]*n
    link = [[] for _ in range(n+1)]
    for i in range(n):
        link[rank[i]] = rank[i+1:]
        cntLink[rank[i]] = i
    
    # 순위 역전
    for _ in range(int(input())):
        a,b = map(int,input().split())
        if a in link[b]:
            link[b].remove(a)
            link[a].append(b)
            cntLink[a] -= 1
            cntLink[b] += 1
        else:
            link[a].remove(b)
            link[b].append(a)
            cntLink[b] -= 1
            cntLink[a] += 1
            
    # 시작 노드
    q = deque()
    for i in range(1,n+1):
        if not cntLink[i]:
            q.append(i)
    if not q:
        # 시작 노드 부재, 사이클
        print("IMPOSSIBLE")
        continue
    
    # 위상 정렬
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for i in link[v]:
            cntLink[i] -= 1
            if not cntLink[i]:
                q.append(i)
    if sum(cntLink) > -1:
        # 사이클 존재
        print("IMPOSSIBLE")
    else:
        print(*ans)