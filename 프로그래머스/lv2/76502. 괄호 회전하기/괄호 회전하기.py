def solution(s):
    
    def check(arr) :
        
        stack = []
        for i in arr :
            if i == '[' or i == '{' or i == '(' :
                stack.append(i)
            elif i == ']' :
                if not stack :
                    return False
                now = stack.pop()
                if now == '[' :
                    continue
                else :
                    return False
            elif i == '}' :
                if not stack :
                    return False
                now = stack.pop()
                if now == '{' :
                    continue
                else :
                    return False
            elif i == ')' :
                if not stack :
                    return False
                now = stack.pop()
                if now == '(' :
                    continue
                else :
                    return False   
        
        if len(stack) > 0 :
            return False
        return True
    
    answer = 0
    
    for i in range(len(s)) :
        arr = s[i:len(s)] + s[0:i]
        if check(arr) :
            answer +=1
    
    return answer