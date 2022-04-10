num = list(range(1,10001))

remove_num = []

for i in range(1, 10000) :
  nums = str(i)
  rm_num = i
  for j in nums :
    rm_num += int(j)
  remove_num.append(rm_num)
remove_num = list(set(remove_num))

for i in remove_num :
  if i in num :
    num.remove(i)

for i in num :
  print(i)