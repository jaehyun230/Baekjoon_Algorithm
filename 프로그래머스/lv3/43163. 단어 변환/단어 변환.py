def solution(begin, target, words):
    INF = int(1e9)
    global answer
    answer = INF
    
    def dfs(start, path) :
        global answer
        for word in words :
            if word not in path :
                count = 0
                flag = True
                for i in range (len(word)) :
                    if start[i] != word[i] :
                        count +=1
                        if count >= 2 :
                            flag = False
                            break
                if flag == True :
                    if word == target :
                        answer = min(answer, len(path)+1)
                    else :
                        dfs(word, path+[word])
                    
    dfs(begin, [])
    if answer == INF :
        return 0
    else :
        return answer