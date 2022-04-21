import sys

input = sys.stdin.readline

def dfs(x, y, shape):
    global answer
    if x == n-1 and y == n-1:
        answer += 1
        return

    if shape == 0 or shape == 2:
        if y + 1 < n:
            if graph[x][y+1] == 0:
                dfs(x, y+1, 0)
    if shape == 1 or shape == 2:
        if x + 1 < n:
            if graph[x+1][y] == 0:
                dfs(x+1, y, 1)
    if shape == 0 or shape == 1 or shape == 2:
        if x + 1 < n and y + 1 < n:
            if graph[x+1][y] == 0 and graph[x][y+1] == 0 and graph[x+1][y+1] == 0:
                dfs(x+1, y+1, 2)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dfs(0, 1, 0)
print(answer)