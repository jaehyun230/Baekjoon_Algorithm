n = int(input())

job = []
benefit = [0] * (n+1)
for _ in range (n) :
  a,b = map(int, input().split())
  job.append((a, b))

for i in range(n) :
  if i+job[i][0] < n+1 :
    for j in range (job[i][1]) :
      if i-j >= 0 :
        benefit[i+job[i][0]] = max(benefit[i-j] + job[i][1], benefit[i+job[i][0]])

print(max(benefit))