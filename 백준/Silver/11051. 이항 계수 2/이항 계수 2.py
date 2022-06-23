n, k = map(int, input().split())

result = 1
for i in range(k):
    result *= n
    n -= 1

divisor = 1
for i in range(2, k+1):
    divisor *= i

print((result // divisor) % 10007)