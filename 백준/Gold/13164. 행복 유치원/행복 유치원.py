import sys

input = sys.stdin.readline

n, k = map(int, input().split())

children = list(map(int, input().split()))

cost = []

for i in range (n-1) :
  cost.append(children[i+1] - children[i])

cost.sort()
print(sum(cost[:n-k]))