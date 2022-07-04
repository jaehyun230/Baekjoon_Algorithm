import sys

input = sys.stdin.readline

n = int(input())

sol = list(map(int, input().split()))

sol.sort()

def binaray_search(start, end, target) :
  val = abs(sol[(start+end)//2] + target)
  cursor = (start+end)//2
  while start <= end :
    mid = (start+end)//2
    if val > abs(sol[mid] + target) :
      cursor = mid
      val = abs(sol[mid] + target)
    if sol[mid] == target*-1 :
      return 0, mid
    if sol[mid] < target*-1 :
      start = mid+1      
    else :
      end = mid-1
             
  return val, cursor
    
answer = [sol[0], sol[1], sol[2]]

for i in range (n-2) :
  for j in range (i+1, n-1) :
    temp = sol[i]+sol[j]
    value, cur = binaray_search(j+1, n-1, temp)
    if abs(sum(answer)) > value :
      answer = [sol[i], sol[j], sol[cur]]
answer.sort()
for i in answer :
  print(i, end=' ')