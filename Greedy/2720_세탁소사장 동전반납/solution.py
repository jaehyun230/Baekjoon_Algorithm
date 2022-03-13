N = int(input())
arr = []
for _ in range(N): # m번 loop을 돌면서 input을 arr에 append
	arr.append(int(input()))
  
for i in range(N) :
  temp = [0, 0, 0, 0]
  while arr[i] > 0 :
    if arr[i] >= 25 :
      arr[i] -=25
      temp[0] +=1
    elif arr[i]>= 10 :
      arr[i] -=10
      temp[1] +=1
    elif arr[i]>= 5 :
      arr[i] -=5
      temp[2] +=1
    elif arr[i]>0 :
      arr[i] -=1
      temp[3] +=1
  print(temp[0],temp[1],temp[2],temp[3])
