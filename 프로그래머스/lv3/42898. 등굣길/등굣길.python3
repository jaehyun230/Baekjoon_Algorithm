def solution(m, n, puddles):
    answer = 0
    
    arr = [[0 for y in range(m+1)] for x in range(n+1)]
    puddles_arr = [[0 for y in range(m+1)] for x in range(n+1)]
    for puddle in puddles:
        puddles_arr[puddle[1]][puddle[0]] = 1
    
    arr[1][1] = 1
    for x in range(1, n+1):
        for y in range(1, m+1):
            if x == 1 and y == 1:
                continue
            if puddles_arr[x][y] == 1:
                continue
            else:
                arr[x][y] = (arr[x-1][y] + arr[x][y-1]) % 1000000007

    return arr[n][m]