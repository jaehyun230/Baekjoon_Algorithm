def solution(stones, k):  
    start = min(stones)
    end = max(stones)

    def check(num) :
        count = k
        for i in range(len(stones)) :
            if stones[i] < num :
                count -=1
                if count == 0 :
                    return False
            else :
                count = k
        return True
    
    while start <= end :
        mid = (start+end)//2
        if check(mid) == False :
            end = mid - 1
        else :
            start = mid + 1
                        
    return start-1