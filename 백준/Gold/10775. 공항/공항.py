import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**4)

g = int(input())
p = int(input())

air_list = [i for i in range(g+1)]

def find(x) :
  if air_list[x] == x :
    return x
  else :
    air_list[x] = find(air_list[x])
    return air_list[x]

count = 0
for _ in range(p) :
  n = int(input())
  result = find(n)
  if result == 0 :
    break

  air_list[result] = air_list[result-1]
  count +=1

for _ in range(p-count-1) :
  n = int(input())

print(count)