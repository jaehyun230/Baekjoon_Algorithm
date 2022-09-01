import copy
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# 감시카메라 종류에 따른 방향
modes = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]],
         [[0, 1], [1, 2], [2, 3], [0, 3]],
         [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]], [[0, 1, 2, 3]]]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 감시구간
def search(board, mode, x, y):
    for i in mode:
        mx = x
        my = y
        while True:
            mx += dx[i]
            my += dy[i]
            if 0 <= mx < n and 0 <= my < m:
                if board[mx][my] == 6:
                    break
                if board[mx][my] == 0:
                    board[mx][my] = 7
            else:
                break

cctv = []

for i in range(n) :
  for j in range(m) :
    if  1 <= graph[i][j] <= 5 :
      cctv.append([graph[i][j], i, j])

def dfs(depth, arr) :
  global answer

  if depth == len(cctv) :
    count = 0
    for i in range(n) :
      count +=arr[i].count(0)
    answer = min(answer, count)
    return

  temp = copy.deepcopy(arr)

  cctv_mode, x, y = cctv[depth]
  for i in modes[cctv_mode]:
    search(temp, i, x, y)
    dfs(depth+1, temp)
    temp = copy.deepcopy(arr)

answer = int(1e9)
dfs(0, graph)
print(answer)
