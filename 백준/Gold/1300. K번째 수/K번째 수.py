#n*n  a[i][j] = i*j
n = int(input())

#오름차순 정렬후 k번째
k = int(input())

def binary_search(target, start, end) :
  while start <= end :
    mid = (start+end) // 2
    count = 0

    for i in range(1, n+1) :
      count += min(mid//i, n)

    if count >= target :
      end = mid-1
    else :
      start = mid+1
      
  return start

print(binary_search(k, 1, n*n))