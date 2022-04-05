n = int(input())

data = [0] * (n+1)
data[1] = 1
if n > 1 :
  data[2] = 2

for i in range (3, n+1) :
  data[i] = data[i-1] + data[i-2]

print(data[n]%10007)
