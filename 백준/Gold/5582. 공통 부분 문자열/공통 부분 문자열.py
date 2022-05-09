arr1 = input()
arr2 = input()

dp = [[0]*(len(arr2)) for _ in range(len(arr1))]

for i in range(len(arr1)) :
  for j in range(len(arr2)) :
    if arr1[i] == arr2[j] :
      if i-1 >=0 and j-1 >= 0 :
        dp[i][j] = dp[i-1][j-1]+1
      else :
        dp[i][j] = 1

answer = 0
for i in dp :
  answer = max(answer, max(i))

print(answer)