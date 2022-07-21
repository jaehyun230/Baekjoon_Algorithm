from collections import defaultdict
from itertools import combinations
def solution(orders, course):
    answer = []
    
    for k in course :
        dic = defaultdict(int)
        for order in orders :
            order = sorted(order)
            menu_candidate = combinations(order, k)
            for menu in menu_candidate :
                temp = ""
                for value in menu :
                    temp +=value
                dic[temp] +=1
        max_count = 0
        for i in dic :
            if dic[i] > max_count :
                max_count = dic[i]
        for i in dic :
            if dic[i] == max_count and max_count>=2 :
                answer.append(i)
    
    answer.sort()
    return answer