import heapq

def solution(food_times, k):
    answer = -1
    
    q = []
    
    for i, food in enumerate(food_times) :
        heapq.heappush(q, [food, i+1])
    
    food_len = len(q)
    past_remain = 0
    
    while q :
        
        time = (q[0][0] - past_remain) * food_len
        
        if k - time >= 0 :
            k -= time
            past_remain, _ = heapq.heappop(q)
            food_len -=1
        
        else:
            idx = k % food_len
            q.sort(key=lambda x: x[1])
            answer = q[idx][1]
            break
        
    return answer