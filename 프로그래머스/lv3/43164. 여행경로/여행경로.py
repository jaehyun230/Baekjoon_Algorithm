from collections import defaultdict

def solution(tickets):
    
    n = len(tickets)
    
    def make_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        
        return routes
    
    routes = make_graph()
    
    for r in routes:
        routes[r].sort()
    
    def dfs(key, path) :
        
        if len(path) == n+1 :
            return path
        
        for idx, route in enumerate (routes[key]) :
            routes[key].pop(idx)
            # deepcopy
            path_list = path[:] 
            path_list.append(route)
            
            result = dfs(route, path_list)
            if result : 
                return result
            # 티켓 반환
            routes[key].insert(idx, route)
    
    answer = dfs("ICN", ["ICN"])
    
    return answer