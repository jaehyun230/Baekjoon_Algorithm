from itertools import combinations

l, c = map(int, input().split())

arr = sorted(input().split())

com = list(combinations(arr, l))

answer = []
for i in com :
  num_v = 0
  num_c = 0
  
  for c in i :
    if c in "aeiou" :
      num_v +=1
    else :
      num_c +=1

    if num_v >=1 and num_c >=2 :
      result = (("".join(i)))
      if result not in answer :
        answer.append(result)

for i in answer:
  print(i)