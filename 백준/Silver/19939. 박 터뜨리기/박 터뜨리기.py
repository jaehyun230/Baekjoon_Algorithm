def solution():
    n, k = map(int, input().split())
    sum_minimum = k*(k+1)//2
    if sum_minimum > n:
        return -1
    if (n-sum_minimum) % k == 0:
        return k-1
    else:
        return k
print(solution())