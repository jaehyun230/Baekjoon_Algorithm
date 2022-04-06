name = input()

dic = {}

for i in name :
  if i not in dic :
    dic[i] = 1
  else :
    dic[i] += 1

count = 0
dict = sorted(dic.items())
side = ""
center = ""
for j in dict :
  if j[1] % 2 != 0 :
    center += j[0]
    count +=1
  side += j[0]*(j[1]//2)

if count > 1 :
  print("I'm Sorry Hansoo")
else :
  print(side+center+side[::-1])