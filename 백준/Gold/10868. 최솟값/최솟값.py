import sys
from math import ceil, log

input = sys.stdin.readline


def minimum(left, right, node_left, node_right, node_num):
    if left > node_right or right < node_left: return 1000000000
    if left <= node_left and right >= node_right: return arr[node_num]
    mid = (node_left + node_right)//2
    return min(minimum(left, right, node_left, mid, node_num*2),
     minimum(left, right, mid+1, node_right, node_num*2 + 1))

def init(size):
    for i in range(size - 1, 0, -1):
        arr[i] = min(arr[i*2], arr[i*2 + 1])
if __name__ == "__main__":
    N, M = map(int,input().split())

    size =  2**ceil(log(N,2))
    size_max = size * 2
    arr = [1000000000]*(size_max)
    for i in range(N):
        arr[size+i]=int(input())
    init(size)
    for _ in range(M):
        s, e = map(int,input().split())
        print(minimum(s-1, e-1, 0, size - 1,1))