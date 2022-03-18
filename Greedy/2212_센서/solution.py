#import sys

n = int(input())
k = int(input())

#which = list(map(int, sys.stdin.readline().split()))
which = list(map(int, input().split()))

which.sort()
dist =[]

if k >= n :
  print(0)
else :
  for i in range (n-1) :
    dist.append(which[i+1]- which[i])

  dist.sort()
  for j in range (k-1) :
    dist.pop(-1)
  print(sum(dist))
