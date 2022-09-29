def solution(files):
    answer = []
    
    index = 0
    for file in files :
        head = ""
        number = ""
        num_check = True
        for i in file :
            if i.isdigit() and len(number) < 5 :
                number += i
                num_check = False
            elif num_check :
                head +=i.upper()
            else :
                break
        
        answer.append([head, int(number), index, file])
        index +=1
    answer.sort()
    
    return [answer[i][3] for i in range(len(answer))]