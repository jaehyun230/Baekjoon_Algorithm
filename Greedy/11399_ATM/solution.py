n = int(input())
time = list(map(int, input().split()))
time.sort()
sum_time = 0
for i in range (n) :
  sum_time += time[i] * (n-i)

print(sum_time)
