def solution(number, k):
    num_list = []
    answer = ''
    
    for i in number:
        
        while num_list and i > num_list[-1] :
            if k > 0 :
                num_list.pop()
                k -=1
            else :
                break
        num_list.append(i)
    
    if k !=0 :
        num_list = num_list[:-k]
    
    answer = ''.join(s for s in num_list)
    
    
    return answer