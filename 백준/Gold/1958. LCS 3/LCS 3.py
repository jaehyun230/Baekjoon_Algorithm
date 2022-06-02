import sys
input = sys.stdin.readline

word1, word2, word3 = input().strip(), input().strip(), input().strip()
h, w, z = len(word1), len(word2), len(word3)

cache = [[[0] *(z+1) for _ in range (w+1) ] for _ in range (h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
      for k in range(1, z+1) :
        if word1[i-1] == word2[j-1] == word3[k-1] :
            cache[i][j][k] = cache[i-1][j-1][k-1] + 1
        else:
            cache[i][j][k] = max(cache[i][j-1][k], cache[i-1][j][k], cache[i][j][k-1])
          
print(cache[-1][-1][-1])