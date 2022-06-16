import sys

input = sys.stdin.readline

n, c = map(int, input().split())

t = int(input())

box = [list(map(int, input().split())) for _ in range (t)]
box.sort(key = lambda x:x[1])

now = [c] * (n+1)
time = 0
answer = 0
for start, end, cost in box :
  _min  = c
  for j in range (start, end) :
    _min = min(_min, now[j])
  _min = min(_min, cost)

  for i in range (start, end) :
    now[i] -= _min
  answer +=_min

print(answer)
  