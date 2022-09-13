import math

def solution(n, k):
    answer = 0
    
    def is_prime_number(x):
        print(x)
        if x <= 1 :
            return False
        # 2부터 x의 제곱근까지의 모든 수를 확인하며
        for i in range(2, int(math.sqrt(x)) + 1):
            # x가 해당 수로 나누어떨어진다면
            if x % i == 0:
                return False # 소수가 아님
        return True # 소수임
    
    def change(n, q):
        rev_base = ''
        while n > 0:
            n, mod = divmod(n, q)
            rev_base += str(mod)

        return rev_base[::-1]
    
    num = change(n, k)
    start = 0
    
    for i in range(len(num)) :
        
        if num[i] == '0' :
            check_num = (num[start:i])
            if len(check_num) > 0 :
                if is_prime_number(int(check_num)) :
                    answer +=1
            start = i+1
    if start < len(num) :
        if is_prime_number(int(num[start::])) :
            answer +=1
    
    return answer