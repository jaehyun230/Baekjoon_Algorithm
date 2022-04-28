import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
 
def dfs(sx, sy):
  # 도착 지점에 도달하면 1(한 가지 경우의 수)를 리턴
  if sx == m-1 and sy == n-1:
    return 1
 
  # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
  if dp[sx][sy] != -1:
    return dp[sx][sy]
    
  ways = 0
  for i in range(4):
    nx, ny = sx + dx[i], sy + dy[i]
    if 0 <= nx < m and 0 <= ny < n and graph[sx][sy] > graph[nx][ny]:
       ways += dfs(nx, ny)
    
  dp[sx][sy] = ways
  return dp[sx][sy]
 
 
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx, dy = [1,-1,0,0], [0,0,1,-1]
 
print(dfs(0,0))