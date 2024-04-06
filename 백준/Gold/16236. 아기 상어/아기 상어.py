from collections import deque

# 아기 상어
# 판 크기
n = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

fishes = []
graph = []

#상어 현재 상태 위치 크기 필요먹이
shark = [-1, -1, 2, 2]

for _ in range(n) :
    graph.append(list(map(int, input().split())))

time = 0

# 상어 시작위치, 물고기 위치 추가
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 9 :
            #상어 위치 업데이트
            shark[0] = i
            shark[1] = j
            graph[i][j] = 0
        elif graph[i][j] != 0 :
            fishes.append((i, j, graph[i][j]))

fishes.sort()

#살아 있는 물고기 체크
aliive_fishes = [True]*len(fishes)

def find_eat() :
    x, y, size, need_eat = shark

    distance = 1000
    number_fish = -1
    find_map = go_eat((x, y))

    for idx, fish in enumerate(fishes) :
        x2, y2, size2 = fish
        if aliive_fishes[idx] == True :
            if size > size2 :
                dis = find_map[x2][y2]
                if dis < distance :
                    distance = dis
                    number_fish = idx

    return (number_fish, distance)

def go_eat(start) :
    q = deque()
    a, b = start
    q.append((a, b, 0))
    visited = [[False]*n for _ in range(n)]
    maps = [[1000]*n for _ in range(n)]
    visited[a][b] = True
    distance = 1000
    while q :
        x, y, d = q.popleft()
        # print("now", x, y, d)

        for i in range(4) :
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < n and 0 <= my < n and visited[mx][my] == False and shark[2] >= graph[mx][my] :
                visited[mx][my] = True
                maps[mx][my] = d+1
                q.append((mx, my, d+1))

    return maps

while True in aliive_fishes :

    num_fish, need_time = find_eat()
    # print("i find fish : ", num_fish, need_time)
    # 먹을수 있는 물고기가 없는 경우
    if num_fish == -1 :
        break
    else :
        now, target = (shark[0], shark[1]), (fishes[num_fish][0], fishes[num_fish][1])

        time = time + need_time
        aliive_fishes[num_fish] = False
        graph[fishes[num_fish][0]][fishes[num_fish][1]] = 0
        # 상어 위치 초기화
        shark[0] = fishes[num_fish][0]
        shark[1] = fishes[num_fish][1]
        # 잡아먹기
        shark[3] = shark[3] - 1
        # 먹고 필요 숫자 만큼 먹은 경우 상어 크기 키우기 and 필요 갯수 초기화
        if shark[3] == 0 :
            shark[2] = shark[2] + 1
            shark[3] = shark[2]

            # print("shark", shark)

print(time)