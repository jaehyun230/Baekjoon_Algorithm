from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[5]*n for _ in range(n)]

trees = [[deque() for _ in range(n)] for _ in range(n)]
dead_trees = [[0]*n for _ in range(n)]
add_graph = []

for i in range(n) :
    add_graph.append(list(map(int, input().split())))

for _ in range(m) :
    x, y, z, = map(int, input().split())
    trees[x-1][y-1].append(z)


year = 0

def spring() :
    for i in range(n) :
        for j in range(n) :
            len_tree = len(trees[i][j])
            for k in range(len_tree) :
                z = trees[i][j].popleft()
                if graph[i][j] >= z :
                    graph[i][j] -=z
                    trees[i][j].append(z+1)
                else :
                    dead_trees[i][j] += z//2

def summer() :
    for i in range(n) :
        for j in range(n) :
            graph[i][j] += dead_trees[i][j]
            dead_trees[i][j] = 0

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def autumn() :

    for i in range(n) :
        for j in range(n) :
            len_tree = len(trees[i][j])
            for k in range(len_tree) :
                if trees[i][j][k] %5 == 0 :
                    for l in range(8):
                        mx = i + dx[l]
                        my = j + dy[l]
                        if 0 <= mx < n and 0 <= my < n:
                            trees[mx][my].appendleft(1)

def winter() :
    for i in range(n) :
        for j in range(n) :
            graph[i][j] += add_graph[i][j]

while year < k :

    spring()
    summer()
    autumn()
    winter()
    year +=1

answer = 0

for i in range(n) :
    for j in range(n) :
        answer += len(trees[i][j])

print(answer)