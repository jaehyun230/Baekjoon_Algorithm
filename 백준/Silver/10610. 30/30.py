num_arr = input()
num_arr = list(num_arr)
num_arr.sort(reverse = True)

sum = 0
if '0' not in num_arr :
  print(-1)
else :
  for i in num_arr :
    sum +=int(i)

  if sum%3 != 0 :
    print(-1)
  else :
    print("".join(num_arr))
  