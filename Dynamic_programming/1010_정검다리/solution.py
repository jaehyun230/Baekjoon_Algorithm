def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num
  
n = int(input())

for _ in range (n) :
  a, b = map(int, input().split())
  print(factorial(b)// (factorial(a) * factorial(b-a)))
