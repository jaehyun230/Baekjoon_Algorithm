from collections import deque
import heapq

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    
    bridge = [0 for _ in range ((bridge_length))]
        
    while bridge :
        bridge.pop(0)
        
        if truck_weights :
            if sum(bridge) + truck_weights[0] <= weight :
                cost = truck_weights.pop(0)
                bridge.append(cost)
            else :
                bridge.append(0)
        answer +=1
    
    return answer