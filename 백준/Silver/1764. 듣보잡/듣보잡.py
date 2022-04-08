import sys

#듣도 못한사람
no_listen = []
#보도 못한사람
no_see = []

n, m = map(int,input().split())

for _ in range(n) :
  no_listen.append(sys.stdin.readline().rstrip())

for _ in range(m) :
  no_see.append(sys.stdin.readline().rstrip())

answer = list(set(no_listen) & set(no_see))
answer.sort()

print(len(answer))
for i in answer:
  print(i)
