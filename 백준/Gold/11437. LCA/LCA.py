import sys
sys.setrecursionlimit(int(1e5)) # 런타임 오류를 피하기 위함
LOG = 21 # 2^20 = 1,000,000

n = int(input())
parent = [[0] * LOG for _ in range(n+1)] # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)] # 그래프 정보

for _ in range (n-1) :
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
#루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x, depth) :
  c[x] = True
  d[x] = depth
  for y in graph[x] :
    if c[y] : # 이미 깊이를 구하였다면
      continue
    parent[y][0] = x
    dfs(y, depth +1)

def set_parent():
  dfs(1, 0)
  for i in range(1, LOG):
    for j in range(1, n+1):
      parent[j][i] = parent[parent[j][i - 1]][i - 1]

def lca(a,b) :
  # b가 더 깊도록 설정
  if d[a] > d[b] :
    a, b = b, a
  #깊이가 동일 하도록 설정
  for i in range(LOG - 1 , -1, -1):
    if d[b] - d[a] >= (1 << i):
      b = parent[b][i]
  #부모가 같아지도록
  if a == b :
    return a
  
  for i in range(LOG - 1 , -1, -1):
    #조상을 향해 거슬러 올라가기
    if parent[a][i] != parent[b][i]:
      a = parent[a][i]
      b = parent[b][i]
  #이후에 부모가 찾고자 하는 조상
  return parent[a][0]
    
set_parent()

m = int(input())

for i in range(m):
  a, b = map(int, input().split())
  print(lca(a,b))
    
 
