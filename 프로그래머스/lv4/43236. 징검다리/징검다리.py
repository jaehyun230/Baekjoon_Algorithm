def solution(distance, rocks, n):
    
    if n == len(rocks) :
        return distance
    
    rocks.sort()
    start = 0
    end = distance
    answer = 0
    
    while start <= end :
        mid = (start+end)//2
        del_count = 0
        pre_rock = 0
        
        for rock in rocks :
            if rock - pre_rock < mid :
                del_count +=1
            else :
                pre_rock = rock
            
            if del_count > n :
                break
        if del_count <=n :
            answer = mid
            start = mid+1
        else :
            end = mid -1
        
    
    return answer