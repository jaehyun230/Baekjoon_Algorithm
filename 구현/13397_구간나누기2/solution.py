import sys
input = sys.stdin.readline

a,b = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)

def isdivided(x) :
  count = 1
  max_val=min_val=data[0]
  for i in range(1,a):
    min_val = min(min_val, data[i])
    max_val = max(max_val, data[i])
    if max_val - min_val > x:
      count+=1
      max_val=data[i]
      min_val=data[i]
  
  return count

result=0
while start < end :
  mid = (start+end) //2

  if isdivided(mid) <= b:
    end = mid - 1
    result=mid
  else :
    start = mid + 1

print(result)
