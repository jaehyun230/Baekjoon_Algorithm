from collections import deque

def solution(gems):
    answer = [1, len(gems)]
    
    num_kind = len(set(gems))
    dic = {}
    start = 0
    end = 0
    
    if num_kind == 1 :
        return [1, 1]

    while end < len(gems) :
        if gems[end] not in dic :
            dic[gems[end]] = 1
        else :
            dic[gems[end]] +=1
        
        if len(dic) == num_kind :
            while start < end :
                if dic[gems[start]] > 1 :
                    dic[gems[start]] -=1
                    start +=1
                elif end - start < answer[1] - answer[0] :
                    answer[1], answer[0] = end+1, start +1
                    break
                else :
                    break
        end +=1
        
    return answer