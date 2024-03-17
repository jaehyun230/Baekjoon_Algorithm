n , m = map(int, input().split())

graph = []

for _ in range(n) :
    data = list(str(input()))
    graph.append(data)


answer = 1

for i in range(n) :
    for j in range(m) :
        for k in range(50) :
            if 0 <= i + k < n and 0<= j + k < m :
                if graph[i][j] == graph[i+k][j] and graph[i][j] == graph[i][j+k] and graph[i][j] == graph[i+k][j+k] :
                    answer = max(answer, (k+1)**2)

print(answer)