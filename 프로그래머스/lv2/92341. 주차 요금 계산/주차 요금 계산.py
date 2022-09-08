import math
from collections import defaultdict

def solution(fees, records):
    answer = []
        
    dic = defaultdict(int)
    result_dic = defaultdict(int)
    
    def dateToMinutes(date):
        h, m = map(int, date.split(':'))
        return h*60 + m
    
    for record in records :
        record = record.split()
        if record[-1] == 'IN' :
            dic[record[1]] = dateToMinutes(record[0])
        if record[-1] == 'OUT' :
            time = dic.pop(record[1])
            result_dic[record[1]] += dateToMinutes(record[0]) - time
    
    # 23:59 처리
    for info in dic :
        time = dic[info]
        result_dic[info] += dateToMinutes("23:59") - time
    
    sort_dic = sorted(result_dic.items())
    
    for num, cost_time in sort_dic :
        
        add = math.ceil((cost_time-fees[0])/fees[2]) * fees[3]
        if add < 0 :
            add = 0
        
        cost = fees[1] + add
        
        answer.append(cost)
    
    return answer