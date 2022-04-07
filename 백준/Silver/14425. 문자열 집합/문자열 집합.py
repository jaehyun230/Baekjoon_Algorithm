import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
count = 0

#집합 S
for _ in range (n) :
  data.append(input())
#문자열 M
for _ in range (m) :
  check = input()
  if check in data : 
    count+=1
  
print(count)