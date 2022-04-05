import sys
input = sys.stdin.readline

n = int(input())

rope = []
for _ in range(n) :
  rope.append(int(input()))

rope.sort(reverse=True)
max_weight = []

for i in range(n) :
  max_weight.append(rope[i]*(i+1))
  
print(max(max_weight))
