#진법, 구할숫자갯수, 참가인원, 순서
def solution(n, t, m, p): 
    answer = ''
    
    #현재 숫자
    now = 0
    #변환진수 남은 숫자갯수
    counter = 1
    #순서
    order = p
    
    def change(num, n) :
        numbers = '0123456789ABCDEF'
        result = ''
        if num == 0 :
            return '0'
        while num > 0 :
            result = numbers[num%n] +result
            num = num // n
        
        return result
    
    now_num = '0'
    while t > 0 :
        counter -=1
        order -=1
        
        if order == 0 :
            answer += now_num[len(now_num)-counter-1]
            order = m
            t -=1
        
        if counter == 0 :
            now +=1
            now_num = change(now, n)
            counter = len(now_num)
            
    return answer