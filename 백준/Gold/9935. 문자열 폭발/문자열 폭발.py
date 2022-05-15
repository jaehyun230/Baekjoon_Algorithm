import sys
input = sys.stdin.readline

#문자열
arr = input().rstrip()
#폭발 문자열
explosion = input().rstrip()
stack = []

for i in arr :
  stack.append(i)
  if "".join(stack[-len(explosion):]) == explosion:
    for i in range(len(explosion)) :
      stack.pop()
    
if len(stack) != 0 :
  print("".join(stack))
else :
  print("FRULA")