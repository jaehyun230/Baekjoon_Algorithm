from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    option = ['*', '+', '-']
    #계산 우선순위 순열
    primarity = permutations(option)
    
    def make_result(priority, expression):
        # arr 만들기
        arr = deque()
        num = ''
        for k in expression:
            if k.isdigit():
                num += k
            else:
                arr.append(num)
                num = ''
                arr.append(k)
        arr.append(num)
        # 계산
        for op in priority:
            stack = []
            while len(arr) != 0:
                temp = arr.popleft()
                if temp == op:
                    result = str(eval(stack.pop()+op+arr.popleft()))
                    stack.append(result)
                else:
                    stack.append(temp)
            arr = deque(stack)
        
        return int(arr.pop())
    
    for case in primarity :
        answer = max(answer, abs(make_result(case, expression)))
        
    return answer