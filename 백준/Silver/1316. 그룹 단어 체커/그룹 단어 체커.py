n = int(input())

count = 0
def check_word(word) :
  result = ""
  for i in word :
    if i not in result :
      result += i
    else :
      if i != result[-1] :
        return 0
  return 1

for _ in range(n) :
  word = input()
  count +=check_word(word)
  
print(count)