import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

start = 0
end = len(arr)-1

answer = abs(arr[start] + arr[end])
result = [arr[start], arr[end]]

while start < end :
  if abs(arr[start] +arr[end]) < answer :
    answer = abs(arr[start] +arr[end])
    result = [arr[start], arr[end]]
    
    
  if arr[start] + arr[end] >= 0 :
    end -=1
  else :
    start +=1
    
print(result[0], result[1])