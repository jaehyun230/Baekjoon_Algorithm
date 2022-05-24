import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
button= list(map(int, input().split()))

start = 100

min_distance = abs(start-target)

for num in range(1000001) :
  num = str(num)
  for i in range(len(num)) :
    if int(num[i]) in button :
      break

    elif i == len(num) - 1 :
      min_distance = min(min_distance, abs(int(num)-target)+len(num))

print(min_distance)