def solution(prices):
    answer = []
    stack = []
    for i in range (len(prices)) :
        value = len(prices) - i - 1
        for j in range(i, len(prices)) :
            if prices[i] > prices[j] :
                value = j - i
                break
        answer.append(value)
            
    return answer