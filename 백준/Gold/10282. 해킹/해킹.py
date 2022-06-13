import sys, heapq
input = sys.stdin.readline
def dijkstra(cur : int):
    virus_cnt, max_time = 0, 0
    hq = [(0, cur)]
    visited = [sys.maxsize] * (N+1)
    visited[cur] = 0
    while hq:
        spend, cur_pos = heapq.heappop(hq)
        if visited[cur_pos] < spend:
            continue
        for next_pos, next_spend in graph[cur_pos]:
            """ 시간초과
            if visited[next_pos] < spend + next_spend:
                continue
            visited[next_pos] = spend + next_spend
            heapq.heappush(hq, (visited[next_pos], next_pos))   
			"""
			# 통과되는 풀이
            if visited[next_pos] > spend + next_spend:
                visited[next_pos] = spend + next_spend
                heapq.heappush(hq, (visited[next_pos], next_pos))

    for i in visited:
        if i == sys.maxsize:
            continue
        virus_cnt += 1
        if max_time < i:
            max_time = i
    return virus_cnt, max_time
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, D, C = map(int, input().split())
        graph = [[] for _ in range(N+1)]
        
        for _ in range(D):
            a, b, s = map(int, input().split())
            graph[b].append((a, s))
        print(*dijkstra(cur=C))