import sys
input = sys.stdin.readline

a = [0] * 11
a[1] = 1
a[2] = 2
a[3] = 4
for i in range (4, 10+1) :
  a[i] = a[i-1] + a[i-2]  + a[i-3] 

n = int(input())

for _ in range (n):
  x = int(input())
  print(a[x])
