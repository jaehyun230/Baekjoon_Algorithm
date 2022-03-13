N = int(input())
arr = []

for _ in range(N): # N번 loop을 돌면서 input을 arr에 append
	arr.append(list(map(int, input().split())))

arr.sort(key = lambda x:(x[1], x[0]))

#회의 끝나는시간
end_time = arr[0][1]
count = 1
#가장 짧은 회의 시작부분은 초기에 카운트
for i in range(1, N) :
  if end_time <= arr[i][0] :
    count +=1
    end_time = arr[i][1]
    
print(count)

