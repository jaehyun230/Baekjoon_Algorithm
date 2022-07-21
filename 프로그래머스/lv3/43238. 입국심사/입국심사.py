def solution(n, times):
    answer = 10**19
    
    start = 0
    end = 10**19
    
    while start <= end :
        count = 0
        mid = (start+end)//2
        for i in times :
            count += mid//i
        
        if count >= n :
            end = mid -1
            answer = min(answer, mid)
        
        else :
            start = mid +1
    
    return answer