input_string = str(input())		# 입력

N = len(input_string)			# 소리 길이
# 소리가 1인 위치 저장
splitter = [i for i in range(N) if input_string[i] == '1']
isSubmarine = False			# 신호 여부
last = -1				# 직전 신호 확인용

if input_string[:2] == '01':		# 맨 처음 수 2개가 '01'이면
    last = 2				# 신호: 2
    
for i in range(1, len(splitter)):	# 1의 위치 기준으로 반복문 실행
    # 1의 위치 기준으로 문자열 자름. 앞쪽 1 제외 뒷쪽 1 포함.
    s_slice = input_string[splitter[i-1] + 1:splitter[i] + 1]
    # 자른 문자열이 '01'이거나 첫 문자열인 경우
    if s_slice == '01' and last != -1:	
        last = 2			# 직전 패턴이 2라 하고 
        continue			# 다음 반복문 실행

    # 1의 위치 기준으로 문자열 자름. 앞쪽 1 포함 뒷쪽 1 포함.
    s_slice = input_string[splitter[i-1]:splitter[i] + 1]
    
    # 자른 문자열이 '11'이고 
    # 직전 패턴이 '100~1~'(1 or 11)이거나 자른 문자열 앞뒤로 '0'이 있을 경우
    # '11' 앞뒤로 '0'이 있는 경우는 1번 패턴 -> 2번 패턴이거나 그 반대인 경우와 1번 패턴 -> 1번 패턴 뿐이다.
    # 2->1 인지는 다음에 판단. 일단 1 -> 1 or 1 -> 2이라고 가정.
    if s_slice == '11' and (last == 1 or last == 11 or (input_string[splitter[i-1]-1:splitter[i]+2] == '0110')):
        last = 11			# 1번 패턴의 마지막임을 알리는 표시
        continue
     
    s_size = len(s_slice)		# 자른 문자열의 길이
    
    if s_size >= 4:			# 자른 문자열의 길이가 4가 넘으면 1번 패턴인지 확인
        # 1번 패턴이라면 자른 문자열은 아래와 같은 문자열이어야 한다.
        s_compare = '100' + ('0' * (len(s_slice) - 4)) + '1'
        if s_slice == s_compare: 	# 비교 후 같다면
            last = 1			# 직전 패턴을 1로 수정
            # 만약 현재 문자열 앞 숫자가 0이라면 소음.
            # 1번 패턴과 2번 패턴 모두 1로 끝남.
            if input_string[splitter[i-1]-1] == '0':
                break
    else:	
        # 문자열 길이가 4보다 작고 '01'도 아니기에 소음이다.
        break
else:
    # 위의 과정을 모두 통과하면 신호이다.
    isSubmarine = True

# 특수한 경우 처리
if input_string[0] == '0' and (N == 1 or (N >= 2 and input_string[:2] != '01')):
    # 길이가 짧거나, 0으로 시작하는데 2번째 수가 1이 아닌 경우
    isSubmarine = False
elif input_string[0] == '1' and N < 4:
    # 1로 시작하는데 길이가 4보다 작은 경우
    isSubmarine = False
elif input_string[-1] == '0':
    # 소리의 끝맺음이 없는 경우
    isSubmarine = False


if isSubmarine:
    print("SUBMARINE")
else:
    print("NOISE")