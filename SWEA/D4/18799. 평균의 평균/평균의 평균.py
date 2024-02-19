def backtrack(S, idx, current, sums, lengths):
    if idx == len(S):  # 모든 요소를 고려했으면
        if current:  # 현재 부분집합이 공집합이 아니라면
            sums.append(sum(current))  # 현재 부분집합의 합 추가
            lengths.append(len(current))  # 현재 부분집합의 길이 추가
        return
    
    # 현재 요소를 포함하는 경우
    backtrack(S, idx + 1, current + [S[idx]], sums, lengths)
    
    # 현재 요소를 포함하지 않는 경우
    backtrack(S, idx + 1, current, sums, lengths)

def average_of_averages(S):
    sums, lengths = [], []
    backtrack(S, 0, [], sums, lengths)
    total_average = sum(sums) / sum(lengths)  # 모든 부분집합의 평균들의 총합을 부분집합의 총 길이로 나눔
    return total_average
    

    
def format_average(avg):
    # 소수점 이하의 길이에 따라 포맷을 동적으로 결정
    if avg == int(avg):  # 소수점 이하가 0이면, 소수점 없이 출력
        return f"{int(avg)}"
    else:
        # 소수점 이하의 실제 길이를 계산
        decimal_part_length = len(f"{avg}".split('.')[1])
        # 최대 20자리까지만 표시
        length = min(20, decimal_part_length)
        format_str = f"{{:.{length}f}}"
        return format_str.format(avg)
    
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    
    numbers = list(map(int, input().split()))
    value = average_of_averages(numbers)
    formatted_avg = format_average(value)
    print(f"#{test_case} {formatted_avg}")

       