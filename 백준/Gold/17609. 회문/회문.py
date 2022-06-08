import sys

input = sys.stdin.readline

n = int(input())

def check(arr) :

  start = 0
  end = len(arr)-1
  count = 0
  while start < end :
    if arr[start] == arr[end] :
      start +=1
      end -=1
    else :
      if arr[start+1] == arr[end] and arr[start] == arr[end-1] :
        if count > 0 :
          return 2
        flag1 = True
        flag2 = True
        x = start+1
        y = end
        while x < y :
          if arr[x] != arr[y] :
            flag1 = False
            break  
          x +=1
          y -=1
          
        x = start
        y = end-1
        while x < y :
          if arr[x] != arr[y] :
            flag2 = False
            break 
          x +=1
          y -=1
        if flag1 == True or flag2 == True :
          return 1
        else :
          return 2
          
      elif arr[start+1] == arr[end] :
        start +=2
        end -=1
        count +=1
      elif arr[start] == arr[end-1] :
        start +=1
        end -=2
        count +=1
      else :
        count = 2
        break
  if count > 2 :
    return 2
  else :
    return count

for _ in range(n) :
  arr = input().rstrip()
  print(check(arr))