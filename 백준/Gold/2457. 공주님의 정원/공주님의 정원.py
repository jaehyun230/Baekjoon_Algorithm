import sys

n = int(sys.stdin.readline())
date = []

# 편의를 위해 100을 곱해 날짜 형식으로 바꿈
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    date.append([temp[0] * 100 + temp[1], temp[2] * 100 + temp[3]])

# 꽃이 피고 지는 날짜를 오름차순으로 정렬
date.sort(key=lambda x:(x[0], x[1]))
# 선택한 꽃의 개수
cnt = 0
# 제일 늦게 지는 꽃을 비교
end = 0
# 마지막 꽃의 지는 날
target = 301

# 모든 꽃이 없어질 때까지 반복하여 꽃을 비교한다.
while date:
    # 마지막 꽃의 지는날이 12월 1일 보다 크거나 같을 때와
    # 마지막 꽃의 지는날이 제일 빨리 피는 꽃보다 작으면 멈춘다.
    if target >= 1201 or target < date[0][0]:
        break

    # 꽃의 개수의 길이만큼 반복하여 구간별로 꽃을 비교한다.
    for _ in range(len(date)):
        # 마지막 꽃의 지는 날이 제일 빨리 피는 꽃보다 크거나 같으면 그 꽃의 지는 날을 확인한다.
        if target >= date[0][0]:
            # 그 꽃의 지는 날과 마지막으로 꽃의 지는 날을 비교한다.
            # 그 꽃의 지는 날이 더 크면 더 오래 꽃을 볼 수 있기때문에
            # 그 꽃의 지는 날을 마지막 꽃의 지는 날로 바꾼다.
            if end <= date[0][1]:
                end = date[0][1]

            # 꽃을 확인 하면 제거한다.
            date.remove(date[0])

        # 꽃의 지는 날이 제일 빨리 피는 꽃보다 작으면 멈춰준다.
        else:
            break

    # 최종적으로 선택한 꽃의 지는 날을 바꾼다.
    target = end
    # 꽃을 선택했으므로 카운트한다.
    cnt += 1

# 마지막 꽃의 지는 날이 12월 1일보다 작으면 11월 30일에는 피어있는 꽃이 없기때문에 0을 출력
if target < 1201:
    print(0)
else:
    print(cnt)