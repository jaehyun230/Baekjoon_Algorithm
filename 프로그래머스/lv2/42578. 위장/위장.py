from collections import defaultdict

def solution(clothes):
    answer = 0
    
    temp = 1
    
    dic = defaultdict(int)
    
    for cloth in clothes :
        dic[cloth[1]] +=1
    
    for val in dic.values() :
        temp *= (val+1)
    
    answer = temp - 1
    
    return answer