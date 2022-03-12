import sys
import math

#강의실 수
n = int(input())
#강의실 별 학생 수
a = list(map(int, input().split()))
#총감독, 부감독 인당 감독가능 인원수
b,c = map(int, input().split())
#각 강의실 별 총감독이 1인 사전 배정
answer = int(n) 
for i in range (n) :
  a[i] -= b
  if(a[i] > 0) :
    answer += (math.ceil(a[i]/c))  
    
print(answer)
