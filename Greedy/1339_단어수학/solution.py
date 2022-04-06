n = int(input())

dic = {}
words = []

for _ in range(n) :
  words.append(input())

for word in words :
  square = len(word)-1
  for i in word :
    if i in dic :
      dic[i] = dic[i] + 10**square
    else: # 없는경우 그대로 넣어준다.
      dic[i] = 10**square
    square -=1

#dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
dic = sorted(dic.values(), reverse=True)

result = 0
for i in range (len(dic)) :
  result += dic[i] * (9-i)

print(result)
