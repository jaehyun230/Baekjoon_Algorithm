import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]


def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]


# 합집합 연산(두 집합을 합치기 위한 함수)
def union_parent(a, b):
  a = find_parent(a)
  b = find_parent(b)
  if a < b:  # 값이 더 작은 쪽을 부모로
    parent[b] = a
  else:
    parent[a] = b


for _ in range(m):
  x, y, z = map(int, input().split())
  if x == 0:
    union_parent(y, z)
  else:
    if find_parent(y) == find_parent(z):
      print('YES')
    else:
      print('NO')