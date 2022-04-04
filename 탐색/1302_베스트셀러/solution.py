import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range (n) :
  data.append(input())
  
top = ''
max_count = 0
data.sort()
for i in data :
  if max_count < data.count(i) : 
    max_count = max(data.count(i), max_count)
    top = i

print(top)
