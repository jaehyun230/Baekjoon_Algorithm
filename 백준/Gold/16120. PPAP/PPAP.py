arr = input()

def check(arr) :
  if arr == "PPAP" or arr == 'P' :
    return True
  
  stack = []
  for i in arr :
    stack.append(i)

    if stack[-4:] == ['P', 'P', 'A', 'P'] :
      for _ in range(3) :
        stack.pop()

  if stack == ['P', 'P', 'A', 'P'] or stack == ['P'] :
    return True
  else :
    return False

if check(arr) :
  print("PPAP")
else :
  print("NP")