import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
INF = int(1e9)
result = INF
# 집의 좌표
house = []
# 치킨집의 좌표
chick = []      

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])
          
# m개의 치킨집 선택
for chi in combinations(chick, m):  
    # 도시의 치킨 거리
    dist = 0            
    for h in house: 
        # 각 집마다 치킨 거리
        chi_len = INF   
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        dist += chi_len
    result = min(result, dist)

print(result)