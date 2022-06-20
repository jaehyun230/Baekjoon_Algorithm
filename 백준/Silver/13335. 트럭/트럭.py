import sys

input = sys.stdin.readline

n, w ,l = map(int, input().split())

truck = list(map(int, input().split()))

bridge = [0] * w

weight, time = 0, 0

while True :
  out = bridge.pop(0)
  weight -= out

  if truck :
    if weight + truck[0] <= l :
      bridge.append(truck[0])
      weight += truck[0]
      truck.pop(0)
    else :
      bridge.append(0)

  time += 1

  if not bridge :
    break

print(time)