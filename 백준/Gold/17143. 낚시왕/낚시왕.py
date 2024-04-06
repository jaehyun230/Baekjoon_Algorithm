# 낚시왕
#행 열 상어 수
n, m, k = map(int, input().split())

shark = []
shark_alive = [True] * k

graph = [
    [[] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for idx in range(k) :
    # 상어 위치, 속력, 방향, 크기
    r, c, s, d, z = map(int, input().split())
    shark.append([r-1, c-1, s, d-1, z, idx])
    # 해당위치 idx 상어 존재
    graph[r-1][c-1].append(idx)

def change_d(d) :
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

def fight(n1, n2) :

    r, c, s, d, z, idx = shark[n1]
    r2, c2, s2, d2, z2, idx2 = shark[n2]

    if z > z2 :
        shark_alive[idx2] = False
        return idx
    else :
        shark_alive[idx] = False
        return idx2

# 상어 상태 업데이트
def update(r, c, s, d, z, idx) :
    shark[idx] = [r, c, s, d, z, idx]

def shark_move(graph) :
   
    new_graph = [
    [[] for _ in range(m)] for _ in range(n)]

    for i in range(k) :
        if shark_alive[i] == True :
            r, c, s, d, z, idx = shark[i]

            for _ in range(s) :
                mr = r + dx[d]
                mc = c + dy[d]
                if 0 <= mr < n and 0 <= mc < m :
                    r, c = mr, mc
                else :
                    d = change_d(d)
                    r = r +dx[d]
                    c = c + dy[d]

            update(r, c, s, d, z, idx)

            # 지금 잘 못된 부분이 모든 이동후 이루어져야함 싸우는 건
            # 이동 후 해당 위치에 상어가 있으면 큰 애가 살아남게 하기
            if new_graph[r][c] :
                idx2 = new_graph[r][c].pop()
                # 해당 상어가 자신일 경우
                if idx == idx2 :
                    new_graph[r][c].append(idx)
                else :
                    num = fight(idx, idx2)
                    new_graph[r][c].append(num)
            # 해당 위치 상어 없으면 상어 생존
            else :
                new_graph[r][c].append(idx)

    graph = new_graph
    
    return graph


start = 0
answer = 0

while start < m :
    # print(graph)
    for i in range(n) :
        if graph[i][start] :
            shark_num = graph[i][start].pop()
            if shark_alive[shark_num] == True :
                # print(shark_num, shark[shark_num][4], i, start)
                answer += shark[shark_num][4]
                shark_alive[shark_num] = False
                break

    graph = shark_move(graph)
    start +=1

print(answer)
