from collections import deque

def solution(maps):
    
    visited = [[0] *len(maps[0]) for _ in range (len(maps))]
    
    
    q = deque()
    q.append((0, 0, 1))
    visited[0][0] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q :
        x, y, c = q.popleft()
        if x == len(maps)-1 and y == len(maps[0])-1 :
            print(visited)
            return c
        
        for i in range(4) :
            mx = x+dx[i]
            my = y+dy[i]
            
            if 0 <= mx < len(maps) and 0<= my < len(maps[0]) and maps[mx][my] == 1 and visited[mx][my] == 0 :
                visited[mx][my] = 1
                q.append((mx, my, c+1))
                      
    return -1