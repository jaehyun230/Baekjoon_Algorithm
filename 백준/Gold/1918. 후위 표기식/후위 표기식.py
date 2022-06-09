import sys

input = sys.stdin.readline

arr = input().rstrip()

stack = []
answer = ""


for i in arr :
  if i == '(' :
    stack.append(i)
  elif i == '*' or i == '/' :
    while stack and (stack[-1] == '*' or stack[-1] == '/'):
      x = stack.pop()
      answer += x
    stack.append(i)
    
  elif i == '+' or i == '-' :
    while stack and stack[-1] != '(' :
      x = stack.pop()
      answer += x
    stack.append(i)
  
  elif i == ')' :
    while stack and stack[-1] != '(':
      x = stack.pop()
      answer +=x
    # ( 빼내기
    stack.pop()
  else :
    answer +=i
    
while stack :
  x = stack.pop()
  answer +=x

print(answer)