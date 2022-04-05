n = int(input())

cost = []

for i in range (n) :
  cost.append(list(map(int, input().split())))

for i in range (1, n) :
  cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
  cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
  cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[n-1]))
