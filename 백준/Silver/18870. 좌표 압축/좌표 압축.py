n = int(input())

number = list(map(int, input().split()))

numbers = list(set(number))
numbers.sort()

num = 0
dic = {}
for i in numbers :
  dic[i] = num
  num +=1

for j in number :
  print(dic[j], end = " ")
