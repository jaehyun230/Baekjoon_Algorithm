n = int(input())

count = 0
for i in range(1, n+1) :
  if i < 100 :
    count +=1
  else :
    num_list = list(map(int,str(i)))
    if num_list[1]-num_list[0] == num_list[2] - num_list[1] :
      count +=1

print(count)