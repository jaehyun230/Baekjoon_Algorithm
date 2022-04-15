import sys

input = sys.stdin.readline

n, m = map(int, input().split())

tree = list(map(int, input().split()))

end = max(tree)
start = 0
top = 0
while start <= end :
  mid = (end+start)//2
  need = 0
  for i in tree :
    if i > mid :
      need += i-mid
  if need >= m :
    top = max(top, mid)
    start = mid +1
  else :
    end = mid - 1

print(top)