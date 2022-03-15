from collections import deque

def bfs_tomatoes(M, N, tomates) :
  count = 0
  deq = deque()
  move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  
  def search(row, col) :
    searched_list = []
    for i, j in move :
      if (row + i < N and col + j < M and row + i >=0 and col + j >=0) :
        if tomatoes[row+i][col+j] == 0 :
          tomatoes[row+i][col+j] = 1
          searched_list.append((row + i, col + j))
    
    return searched_list

  for i in range(N) :
    for j in range(M) :
      if tomates[i][j] == 1 :
        deq.append((i,j))
  
  while deq:
    for _ in range (len(deq)) :
      r, c = deq.popleft()
      for tomato in search(r, c):
        deq.append(tomato)
    count +=1

  for i in range(N) :
    for j in range(M) :
      if tomates[i][j] == 0 :
        return -1
  
  return count - 1

M, N = map(int, input().split(" "))
tomatoes = [[int(n) for n in input().split(" ")] for _ in range(N)]
print(bfs_tomatoes(M, N, tomatoes))
