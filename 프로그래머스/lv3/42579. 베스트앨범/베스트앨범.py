import heapq
from collections import defaultdict

def solution(genres, plays):
    
    answer = []
    
    dic = {}
    
    q = []
    
    for i in range (len(genres)) :
        if genres[i] not in dic :
            dic[genres[i]] = plays[i]
        else :
            dic[genres[i]] += plays[i]
        q.append((genres[i], plays[i], i))
    
    
    dic = sorted(dic.items(), key = lambda x: -x[1])
    
    q.sort(key = lambda x : (x[0], -x[1], x[2]) )
    
    type_count = 0
    
    while type_count != len(dic) :
        count = 0
        for i in q :
            if i[0] == dic[type_count][0] :
                answer.append(i[2])
                count +=1
                if count == 2:
                    break
        
        type_count +=1
    
    return answer