import sys
input = sys.stdin.readline

n = int(input())

count = {}

num_list = []
for i in range (n) :
  num_list.append(int(input()))

sum = 0
small = int(1e-9)
for i in num_list :
  sum += i

num_list.sort()

for i in num_list :
  if i not in count :
    count[i] = 1
  elif i in count :
    count[i] +=1

count = sorted(count.items(), key = lambda x: (x[1], -x[0] ), reverse = True)

#산술평균
print(round(sum/n+small))
#중간값
print(num_list[len(num_list)//2])
#카운트
if len(count) > 1 :
  if count[0][1] == count[1][1] :
    print(count[1][0])
  else :
    print(count[0][0])
else :
  print(count[0][0])

#범위
print(max(num_list)-min(num_list) )