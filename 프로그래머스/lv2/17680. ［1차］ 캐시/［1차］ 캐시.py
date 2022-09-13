from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()
    
    for city in cities :
        if city.upper() in q :
            answer +=1
            q.remove(city.upper())
        else :
            answer +=5
        q.append(city.upper())
        if len(q) > cacheSize :
            q.popleft()
    
    return answer