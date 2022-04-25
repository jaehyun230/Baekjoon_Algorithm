import sys

input = sys.stdin.readline

y, x, time = map(int, input().split())

graph = []
for _ in range (y) :
  graph.append(list(map(int, input().split())))

air_clean = 0
#공기청정기 위치 찾기
for i in range (2, y-2) :
  if graph[i][0] == -1 :
    air_clean = i
    break

#회전 time 횟수
for t in range (time) :
  temp_graph = [[0] * x for _ in range(y)]
  for i in range (y) :
    for j in range (x) :
      if graph[i][j] != -1 :
        count_b = 0
        # 공기 확산
        if i-1 >= 0 and graph[i-1][j] != -1 :
          temp_graph[i][j] += graph[i-1][j]//5
          count_b +=1
        if j-1 >= 0 and graph[i][j-1] != -1 :
          temp_graph[i][j] += graph[i][j-1]//5
          count_b +=1
        if i+1 < y and graph[i+1][j] != -1 :
          temp_graph[i][j] += graph[i+1][j]//5
          count_b +=1
      # 청정기는 1열에있음으로 오른쪽칸은 -1 확인 필요 x
        if j+1 < x :
          temp_graph[i][j] += graph[i][j+1]//5
          count_b +=1
        #자신의 공기 확산하고 있는 공기
        temp_graph[i][j] += graph[i][j] - (graph[i][j]//5) * count_b
         
  #공기 청정기 윗방향
  for h in range (air_clean-1, 0, -1) :
    temp_graph[h][0] = temp_graph[h-1][0]
  for k in range (x-1) :
    temp_graph[0][k] = temp_graph[0][k+1]
  for h in range (air_clean) :
    temp_graph[h][x-1] = temp_graph[h+1][x-1]
  for k in range (x-2, 0, -1) :
    temp_graph[air_clean][k+1] = temp_graph[air_clean][k]
  temp_graph[air_clean][1] = 0

  #공기 청정기 아랫방향
  for h in range(air_clean+1, y-1) :
    temp_graph[h][0] = temp_graph[h+1][0]
  for k in range(x-1) :
    temp_graph[y-1][k] = temp_graph[y-1][k+1]
  for h in range(y-1, air_clean, -1) :
    temp_graph[h][x-1] = temp_graph[h-1][x-1]
  for k in range(x-1, 0, -1) :
    temp_graph[air_clean+1][k] = temp_graph[air_clean+1][k-1]
  
  temp_graph[air_clean+1][1] = 0

  graph = temp_graph
  graph[air_clean][0] = -1
  graph[air_clean+1][0] = -1
  
answer = 0
for i in graph :
  answer +=sum(i)

print(answer+2)
