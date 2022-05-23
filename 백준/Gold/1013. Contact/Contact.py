import sys

input = sys.stdin.readline

t = int(input())

for _ in range (t) :
  arr = input().rstrip()
  cursor = 0
  
  answer = "YES"
  
  while cursor < len(arr) :
    if arr[cursor:cursor+3] == "100" :
      cursor +=3

      while cursor < len(arr) and arr[cursor] == '0' :
        cursor +=1
      if cursor == len(arr) :
        answer = "NO"
        break
      if arr[cursor] == '1' :
        cursor +=1
      else :
        answer = "NO"
        break

      while cursor < len(arr) and arr[cursor] == '1' :
        if cursor+2 < len(arr) and arr[cursor:cursor+3] == "100" :
          break
        else :
          cursor+=1
      
    elif arr[cursor:cursor+2] == "01" :
      cursor +=2
    else :
      answer = "NO"
      break

  print(answer)