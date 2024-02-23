import heapq

import sys

input = sys.stdin.readline

n = int(input())

deck = []

for _ in range (n) :
  heapq.heappush(deck, int(input()))

answer = 0
while len(deck) >= 2 :
  card1 = heapq.heappop(deck)
  card2 = heapq.heappop(deck)
  answer += card1 + card2
  heapq.heappush(deck, card1+card2)

print(answer)