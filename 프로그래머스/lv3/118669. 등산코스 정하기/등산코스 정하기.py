from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):

    gates.sort()
    summits.sort()
    graph = defaultdict(list)
    
    for a,b,c in paths :
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    def dijkstra() :
        
        visited = [10000001] * (n+1)
        q = []
        for gate in gates :
            heapq.heappush(q, [0, gate])
            visited[gate] = 0
        
        while q :
            intensity, now = heapq.heappop(q)
            if now in summits_set :
                continue
            if visited[now] < intensity :
                continue
            
            for target, cost in graph[now] :
                new_intensity = max(intensity, cost)
                if visited[target] > new_intensity :
                    visited[target] = new_intensity
                    heapq.heappush(q, [new_intensity, target])
        
        result = [0, 10000001]
        for summit in summits:
            if visited[summit] < result[1]:
                result[0] = summit
                result[1] = visited[summit]
                
        return result
    
    summits_set = set(summits)
        
    answer = dijkstra()
    
    return answer