def solution(msg):
    answer = []
    
    dic = dict()
    char_list = []    
    [char_list.append(chr(i)) for i in range(ord('A'), ord('Z')+1)]

    for index, ch in enumerate(char_list) :
        dic[ch] = index+1
    
    now = 0
    length = 0
    max_dic = 26
    
    while now+length-1 <= len(msg) :
        
        length +=1
        
        if not msg[now:now+length] in dic :
            answer.append(dic[msg[now:now+length-1]])
            #사전에 새로 추가
            max_dic +=1
            dic[msg[now:now+length]] = max_dic
            now += length -1
            length = 0
        else :
            if now+length-1 == len(msg):
                answer.append(dic[msg[now:now+length-1]])
                break
                
    return answer