
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    sales = list(map(int, input().split()))
    answer = []
    dic = {}
    for sale in sales :
        
        sale_cost = (sale//4 *3)
        if sale_cost in dic and dic[sale_cost] > 0 :
            answer.append(sale_cost)
            dic[sale_cost] -=1
        elif sale not in dic :
            dic[sale] =1
        else :
            dic[sale] +=1
    
    print("#"+str(test_case), end=" ")
    for a in answer :
        print(a, end =" ")
    print()
    
    
