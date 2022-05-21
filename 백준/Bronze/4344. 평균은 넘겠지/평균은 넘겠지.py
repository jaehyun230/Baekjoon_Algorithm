n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    # 평균 구하기 (nums[0]: 학생수, nums[1:] 점수)
    avg = sum(nums[1:])/nums[0]  
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            # 평균 이상 학생 수
            cnt += 1  
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')