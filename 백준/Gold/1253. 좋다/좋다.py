from collections import defaultdict

n = int(input())

nums = list(map(int, input().split()))

dic = defaultdict(list)

nums.sort()

for i in range(len(nums)) :
    dic[nums[i]].append(i)


answer = 0
check = [0] * (n+1)
for i in range(n) :
    for j in range(n) :
        if i == j :
            continue
        if nums[i] + nums[j] in dic :

            for k in dic[nums[i]+nums[j]] :
                if k != i and k != j :
                    check[k] = 1
                    dic[nums[i]+nums[j]].remove(k)

print(check.count(1))