#플러그 구멍, 전기용품 사용횟수
n, k = map(int, input().split())
#전기용품 사용 순서 번호 리스트
use_order = list(map(int, input().split()))
#사용중 전기제품
use_list = []

count = 0
for i in range (k) :
  if use_order[i] not in use_list :
    if len(use_list) == n :
      remove_data = use_list[0]
      priority = 0
      for j in range (len(use_list)) :
        try :
          if priority < use_order.index(use_list[j],i+1,k+1) :
            priority = use_order.index(use_list[j],i+1,k+1)
            remove_data = use_list[j]
          
        except :
          remove_data = (use_list[j])
          break
      use_list.remove(remove_data)  
      count +=1
      
    use_list.append(use_order[i])

print(count)

