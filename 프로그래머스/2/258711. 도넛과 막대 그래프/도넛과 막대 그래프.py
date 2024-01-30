from collections import deque

def solution(edges):
    MAXLEN = 1000001

    go = [[] for _ in range(MAXLEN)]
    take = [[] for _ in range(MAXLEN)]
    for a, b in edges:
        go[a].append(b)
        take[b].append(a)

    start = -1
    for node in range(1_000_002):
        if len(take[node])==0 and len(go[node])>=2:
            start = node
            break

    ans = [start, 0, 0, 0] # 시작, 도넛, 막대, 8자
    visited = [False] * (MAXLEN)

    def bfs(i):
        q = deque([i])
        visited[i] = True

        while q:
            node = q.popleft()
            if not go[node]: # 막대
                ans[2] += 1
                return
            if len(go[node])==2 and len(take[node])==2: # 8자
                ans[3] += 1
                return
            for next_node in go[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node) 

        ans[1] += 1

    for node in go[start]:
        take[node].remove(start)
        bfs(node)

    return ans