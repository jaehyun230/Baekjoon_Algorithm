from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    
    history_dic = defaultdict(int)
    point_dic = defaultdict(int)
    
    for gift in gifts :
        sender, receiver = gift.split()
        
        point_dic[sender] +=1
        point_dic[receiver] -=1
        history_dic[(sender, receiver)] +=1
    
    for i in friends :
        present = 0
        for j in friends :
            if history_dic[(i, j)] > history_dic[(j, i)] :
                present +=1
            elif history_dic[(i, j)] == history_dic[(j, i)] :
                if point_dic[i] > point_dic[j] :
                    present +=1
        answer = max(answer, present)
    
    return answer