from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())

A, B, C, D = [], [], [], []

for _ in range (n) :
  x, y, z, k = map(int, input().split())
  A.append(x)
  B.append(y)
  C.append(z)
  D.append(k)
#정렬
A.sort()
B.sort()
C.sort()
D.sort()

dic1 = defaultdict(int)
dic2 = defaultdict(int)


for i in range(n) :
  for j in range(n) :
    val = A[i] + B[j]
    if A[i]+B[j] not in dic1 :
      dic1[val] = 1
    elif A[i]+B[j] in dic1 :
      dic1[val] +=1

answer = 0
for i in range(n) :
  for j in range(n) :
    val = (C[i] + D[j]) *-1
    if val in dic1 :
      answer +=dic1[val]

print(answer)