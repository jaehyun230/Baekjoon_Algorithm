from collections import deque
import sys

n = int(input())

k = int(input())

visited = [[False] * n for _ in range(n)]
graph = [[0]*n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(k) :
    #사과 위치
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

l = int(input())

q = deque()
q.append((0, 0, 1))
visited[0][0] = True
now = 0
alive = True

def move(x1,y1, direct) :
    mx = x1 + dx[direct]
    my = y1 + dy[direct]
    q.append((x1, y1, direct))

    if 0 <= mx < n and 0<= my < n and visited[mx][my] == False :
        visited[mx][my] = True
        if graph[mx][my] == 1 :
            graph[mx][my] = 0
        else :
            #꼬리 제거
            x2, y2, d2 = q.popleft()
            visited[x2][y2] = False
        q.append((mx, my, direct))
    else :

        return False
    return True

for _ in range(l) :
    t, d = input().split()
    t = int(t)

    while now < t and alive == True :
        x, y, direction = q.pop()

        if move(x, y, direction) == False :
            alive = False
        now +=1

    if now == t :
        x, y, direction = q.pop()
        if d == 'L':
            direction = (direction - 1) % 4
        elif d == "D":
            direction = (direction + 1) % 4
        q.append((x, y, direction))

while alive == True :
    x, y, direction = q.pop()
    if move(x, y, direction) == False:
        alive = False
    now += 1

print(now)