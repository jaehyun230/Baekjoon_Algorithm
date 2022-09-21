import heapq

def solution(n, s, a, b, fares):
    
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    
    for x, y, z in fares :
        graph[x].append([y, z])
        graph[y].append([x, z])
    
    
    def dijkstra(start, end) :
        q = []
        heapq.heappush(q, (0, start))
        dist = [INF] * (n+1)
        dist[start] = 0
        while q :
            cost, now = heapq.heappop(q)
            if now == end :
                return cost
            for x, y in graph[now] :
                
                if dist[x] > cost+y :
                    dist[x] = cost+y
                    heapq.heappush(q, (cost+y, x))
        return INF
    
    answer = INF
    
    for p in range(1, n+1):
        if p != s:
            s_to_p = dijkstra(s,p)
            p_to_a = dijkstra(p,a)
            p_to_b = dijkstra(p,b)
            answer = min(s_to_p+p_to_a+p_to_b, answer)
        else:
            answer = min(dijkstra(s,a)+dijkstra(s,b), answer)
    
    return answer