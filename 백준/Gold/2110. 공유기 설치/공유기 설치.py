import sys

input = sys.stdin.readline

n, c = map(int, input().split())

house = [int(input()) for _ in range(n)]

house.sort()
#일정길이 이상체크
def check(num, c) :
  now = house[0]
  count = 1
  for i in range(1, len(house)) :
    if house[i] >= now + num :
      count +=1
      now = house[i]

  if count >= c :
    return True
  else :
    return False

start = 0
end = 1000000000

answer = 0
while start <= end :
  mid = (start+end)//2
  if check(mid, c) :
    answer = mid
    start = mid+1
  else :
    end = mid-1

print(answer)