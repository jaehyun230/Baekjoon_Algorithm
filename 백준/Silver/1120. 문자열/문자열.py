arr = input()

#arr1이 arr2보다 짧거나 같음
arr1, arr2 = arr.split()

answer = []
for i in range (len(arr2) - len(arr1) + 1) :
  #차이값
  count = 0
  for j in range(len(arr1)) :
    if arr1[j] != arr2[i+j] :
      count +=1
  answer.append(count)

print(min(answer))