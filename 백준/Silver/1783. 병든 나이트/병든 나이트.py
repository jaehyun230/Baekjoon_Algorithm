n, m = map(int, input().split())

#n 세로, m 가로
if n == 1 :
  print(1)
elif n == 2:
  print(min(4, (m-1)//2+1))
elif m <= 6:
    print(min(4, m))
else :
  print(m-2)