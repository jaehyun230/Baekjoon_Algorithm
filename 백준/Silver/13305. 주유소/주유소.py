n = int(input())

dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]
answer = 0
for i in range(len(dist)) :
  min_cost = min(min_cost, cost[i])
  answer += dist[i]*min_cost

print(answer)