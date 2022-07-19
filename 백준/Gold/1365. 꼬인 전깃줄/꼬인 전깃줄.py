import bisect

n = int(input())

arr = list(map(int, input().split()))

result = [arr[0]]

for i in range (1, len(arr)) :
  index = bisect.bisect_left(result, arr[i])
  if index == len(result):
    result.append(arr[i])
  else:
    result[index] = arr[i]

print(len(arr) - len(result))