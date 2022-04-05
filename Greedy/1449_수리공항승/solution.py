import sys
input = sys.stdin.readline

#테스트 케이스 수
t, l = map(int, input().split())

need = list(map(int, input().split()))
need.sort()

start = need[0]
end = start + l - 0.5
count = 1
for i in need :
  if end > i :
    continue
  else :
    count +=1
    end = i + l -0.5

print(count)
