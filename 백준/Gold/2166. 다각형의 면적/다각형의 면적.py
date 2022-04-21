import sys

input = sys.stdin.readline
n = int(input())
polygon = []

for _ in range(n) :
  x,y = map(int, input().split())
  polygon.append((x, y))
  
polygon.append((polygon[0][0], polygon[0][1]))

sum_x = sum_y = 0
#면적 계산
for i in range(n):
  sum_x += polygon[i][0] * polygon[i+1][1]
  sum_y += polygon[i][1] * polygon[i+1][0]

#소수점 둘째자리까지 반올림
answer = abs((round((sum_x - sum_y)/2, 1)))

print(answer)
