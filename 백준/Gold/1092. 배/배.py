#크레인수
n = int(input())
crane = list(map(int, input().split()))
#무거운 순으로 정렬
crane.sort(reverse = True)
#박스 수
m = int(input())
box = list(map(int, input().split()))
box.sort(reverse = True)
#옮긴 박스 확인
checked = [0 for _ in range(m)]
#걸리는 시간
time = 0
#체크 위치
positions = [0 for _ in range(n)]

#옮긺 수 없는 경우
if max(box) > max(crane):
    print(-1)
else:
    while 0 in checked :
        for i in range(n): # 크레인에 대하여
            while positions[i] < len(box):
            # 아직 안 옮긴 박스 중에서, 옮길 수 있는 박스를 만날 때까지 반복
                if not checked[positions[i]] and crane[i] >= box[positions[i]]:
                    checked[positions[i]] = True
                    positions[i] += 1                    
                    break
                positions[i] += 1
        time += 1
    print(time)    