import heapq
import sys

input = sys.stdin.readline

n = int(input())

q = []

for _ in range(n):
    q.append(int(input()))

q.sort()

answer = 0
while len(q) >= 2:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    answer += a + b
    heapq.heappush(q, a + b)

print(answer)