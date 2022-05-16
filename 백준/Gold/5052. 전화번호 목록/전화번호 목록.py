import sys

input = sys.stdin.readline

#테스트 케이스 수
t = int(input())

for _ in range (t) :
  n = int(input())
  number = []
  for _ in range (n) :
    num = input().rstrip()
    number.append(num)
  number.sort()
  #일관성 플래그
  flag = True
  for i in range (len(number)-1) :
    for j in range (i+1, len(number)) :
      if number[i] == number[j][0:len(number[i])] :
        flag = False
        break
  if flag :
    print("YES")
  else :
    print("NO")