from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,h,d = map(int, input().split())
board = []

sx=sy=-1
for x in range(n):
    board.append(list(input().strip()))
    if sx==-1:
        for y in range(n):
            if board[x][y] == 'S':
                sx,sy = x,y

def solv():
    visited = [[0]*n for _ in range(n)]
    q = deque([(sx,sy,h,0,0)])
    visited[sx][sy] = h

    while q:
        x,y,now_h,now_d,cnt = q.pop()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if point_validator(nx,ny):
                if board[nx][ny] == 'E':
                    print(cnt+1)
                    return
                nxt_h = now_h
                nxt_d = now_d

                if board[nx][ny] == 'U':
                    nxt_d = d

                if nxt_d == 0:
                    nxt_h -= 1
                else:
                    nxt_d -= 1

                if nxt_h == 0:
                    continue

                if visited[nx][ny] < nxt_h + nxt_d:
                    visited[nx][ny] = nxt_h + nxt_d
                    q.appendleft((nx,ny,nxt_h,nxt_d,cnt+1))

    print(-1)
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True
solv()