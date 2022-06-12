import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))
num.sort()

mid = (len(num)-1)//2

print(num[mid])