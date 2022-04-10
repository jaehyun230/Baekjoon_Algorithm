n = int(input())

data = []
rank = []
for _ in range(n) :
  x,y = map(int, input().split())
  data.append((x, y))

for i in data :
  count = 1
  for j in data :
    if i[0] < j[0] and i[1] < j[1] :
      count +=1
  rank.append(count)

for i in rank :
  print(i, end = " ")