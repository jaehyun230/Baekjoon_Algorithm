n,m = map(int, input().split())

cost_set = []
cost_one = []

for i in range (m) :
  a, b = map(int, input().split())
  cost_set.append(a)
  cost_one.append(b)

answer = 0
if n % 6 == 0 :
  answer =  min (n//6 * min(cost_set), n//1 * min(cost_one))
else :
  answer = min ( (n//6 +1) * min(cost_set), n//1 * min(cost_one), 
               n//6 * min(cost_set) + n%6 * min(cost_one))
  
print(answer)