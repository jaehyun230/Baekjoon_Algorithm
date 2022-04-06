import sys
input = sys.stdin.readline

n, k = map(int, input().split())

money = []
for _ in range (n) :
  money.append(int(input()))

count = 0
while k > 0 :
  for i in range (n-1, -1, -1) :
    if k >= money[i] :
      count += k//money[i]
      k = k%money[i]

print(count)
