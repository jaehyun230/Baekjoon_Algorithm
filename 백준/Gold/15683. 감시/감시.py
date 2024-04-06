import copy
import sys

sys.setrecursionlimit(10**6)

n, m = map(int ,input().split())

graph = []
CCTV = []

for _ in range(n) :
    graph.append(list(map(int, input().split())))

for i in range(n) :
    for j in range(m) :
        if graph[i][j] != 0 and graph[i][j] != 6 :
            CCTV.append((i, j, graph[i][j]))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

modes = [[],
         [[0], [1], [2], [3]],
         [[0, 2], [1, 3]],
         [[0, 1], [1, 2], [2, 3], [3, 0]],
         [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
         [[0, 1, 2, 3]]
         ]


answer = (n+1) * (m+1)

def search(a, b, d, arr) :
    x, y = a, b
    for k in range(max(n, m)) :
        x = x + dx[d]
        y = y + dy[d]
        if 0<= x < n and 0 <= y < m and arr[x][y] != 6 :
            if arr[x][y] == 0 :
                arr[x][y] = -1
        else :
            break

def calculate(arr) :
    global answer
    count = 0
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 0 :
                count +=1

    answer = min(answer, count)
def dfs(idx, arr) :

    if idx == len(CCTV) :
        calculate(arr)
        return

    x, y, type = CCTV[idx]
    temp = copy.deepcopy(arr)

    for i in modes[type] :
        for j in i :
            search(x, y, j, temp)
        dfs(idx+1, temp)
        temp = copy.deepcopy(arr)

    return

dfs(0, graph)

print(answer)