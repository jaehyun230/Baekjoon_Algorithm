import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# Binary_search method 속도개선을 위함 (dp 사용시 시간초과)
def binary_search(lis_arr, num): #

    low = -1 # 접근 X
    high = len(lis_arr) # 접근 X

    # 결정 문제
    # [1 3 5] 에서 2가 들어오면 [2 3 5]가 되어야 함

    # num은 mid보다 큰가? -> TF문제에서 가장 작은 F (high)
    # 왜 초과인가? -> 같은 숫자가 들어올 수 있기 때문
    
    while low +1 < high:
        
        mid = (low + high)//2 
        # TTF므로 왼쪽 탐색 X
        if num > lis_arr[mid]: 
            low = mid
        else:
            high = mid

    return high

#값 범위 
lis_arr = [-1000000001]
lis_total = [(-1000000001,0)] 

nums = nums[::-1] # stack처럼 쓰기 위해

while nums:
    num = nums.pop()

    if num > lis_arr[-1]:
        lis_total.append((num, len(lis_arr)))
        lis_arr.append(num)

    else:
        idx = binary_search(lis_arr, num)
        lis_arr[idx] = num
        lis_total.append((num, idx))

lis_length = len(lis_arr)-1
lis = []

while lis_total and lis_length:
    num, idx = lis_total.pop()
    if idx == lis_length:
        lis.append(num)
        lis_length -= 1

lis.reverse()
print(len(lis))
print(*lis)