n, m = map(int, input().split())

answer = []

numbers = list(map(int, input().split()))
numbers.sort()
visited = [False] * len(numbers)


def backtrack(now) :
    if len(now) == m :
        for i in now :
            print(i, end = " ")
        print()

    else :
        remember = 0
        for i in range(n) :
            if visited[i] == False and remember != numbers[i]:
                visited[i] = True
                remember = numbers[i]
                backtrack(now + [numbers[i]])
                visited[i] = False

backtrack([])