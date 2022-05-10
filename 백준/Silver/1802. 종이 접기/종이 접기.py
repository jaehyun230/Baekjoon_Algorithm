import sys

input = sys.stdin.readline

t = int(input())

#가운데를 기준으로 대칭값들이 반대이어야함
def check(num):
    if len(num) == 1:
        return True
    for i in range(len(num)//2):
        if num[i] == num[len(num)-1-i]:
            return False
    return check(num[0:len(num)//2]) and check(num[len(num)//2+1:len(num)])

for _ in range (t) :
  num = input().rstrip()
  flag = check(num)
  if flag :  
    print("YES")
  else :
    print("NO")