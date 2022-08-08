import sys

input = sys.stdin.readline

n, m = map(int, input().split())

k = int(input())

x_list = [0]
x_list.append(m)
y_list = [0]
y_list.append(n)

for _ in range (k) :
  a, b = map(int, input().split())
  if a == 0 :
    x_list.append(b)
  else :
    y_list.append(b)

x_list.sort()
y_list.sort()

answer = 0

for i in range (len(x_list)-1) :
  for j in range(len(y_list)-1) :
    x = x_list[i+1] - x_list[i]
    y = y_list[j+1] - y_list[j]
    answer = max(answer, x*y)

print(answer)