L = int(input())
M = 1234567891
r = 31
data = input()
 
answer = 0
 
for i in range(len(data)):
    # 아스키코드값 변환
    num = ord(data[i]) - 96
    answer += num * (r ** i)
 
print(answer % M)