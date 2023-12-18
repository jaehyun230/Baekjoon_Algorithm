def solution(users, emoticons):
    answer = []
    discounts = []
    
    def dfs(path) :
        discount = [10, 20, 30, 40]
        if len(path) == len(emoticons) :
            discounts.append(path)
            return
        else :
            for dis in discount :
                dfs(path + [dis])
                      
    dfs([])
    
    result_user = 0
    result_price = 0
    
    for discount in discounts :
        service_price = 0
        service_user = 0
        for user in users :
            user_price = 0
            for i in range( len(emoticons)) :
                
                if (discount[i] >=  user[0]) :
                    price = emoticons[i] * (100-discount[i])/100
                    
                    user_price +=price
            
            if(user_price >= user[1]) :
                service_user +=1
            else :
                service_price += user_price
        
        if service_user > result_user :
            result_user = service_user
            result_price = service_price
        elif service_user == result_user :
            result_price = max(result_price, service_price)
    
    
    return [result_user, result_price]
                
                
                    
                
            
            
            
    
    return answer