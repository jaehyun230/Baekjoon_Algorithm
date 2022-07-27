import heapq

def solution(jobs):
    
    
    q = []
      
    answer = 0
    now = 0
    count = 0
    start = -1
    while count < len(jobs) :
        for job in jobs :
            if start < job[0] <= now :
                heapq.heappush(q, (job[1], job[0]))
        
        if len(q) > 0 :
            current = heapq.heappop(q)
            start = now
            now += current[0]
            answer += (now - current[1])
            count +=1
        else :
            now +=1
                
        
    return int(answer//len(jobs))