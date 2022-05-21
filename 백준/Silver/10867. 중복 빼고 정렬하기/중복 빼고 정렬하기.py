n = int(input())
num = list(map(int, input().split()))
number = []
for i in num :
  if i not in number :
    number.append(i)

number.sort()
for i in number :
  print(i, end =" ")
           