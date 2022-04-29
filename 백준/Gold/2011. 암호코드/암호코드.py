n = list(map(int, list(input())))
l = len(n)

dp = [0] * (len(n)+1)

#암호 생성 불가능한 경우
if n[0] == 0 :
  print(0)

else :
  #인덱싱 갑 계산위해 추가
  n = [0] + n
  dp[0] = 1
  dp[1] = 1

  for i in range(2, l+1) :
    #한자리
    cur = n[i]
    #두자리
    cur2 = n[i-1] * 10 +n[i]
    if cur >= 1 and cur <= 9 :
      dp[i] += dp[i-1]
    if cur2 >=10 and cur2 <=26 :
      dp[i] += dp[i-2]
    dp[i] %= 1000000

  print(dp[l])