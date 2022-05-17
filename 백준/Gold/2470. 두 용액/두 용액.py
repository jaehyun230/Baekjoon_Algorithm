import sys

input = sys.stdin.readline
#입력 숫자 갯수
n = int(input())
#숫자 입력
num = list(map(int, input().split()))
#숫자 정렬
num.sort()
#가장 작은값 찾기
def search(start, end) :

  check = abs(num[start] + num[end])
  answer = [start, end]
  
  while start < end :
    l_val = num[start]
    r_val = num[end]
    total = (l_val + r_val)
    
    if check > abs(total) :
      check = abs(total)
      answer = [start, end]
    
    if total < 0 :
      start += 1
      
    else :
      end -=1

  return answer 

left, right = search(0, n-1)
print(num[left], num[right])