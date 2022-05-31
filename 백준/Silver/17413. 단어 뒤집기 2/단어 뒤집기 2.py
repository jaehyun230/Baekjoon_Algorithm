import sys
word = list(sys.stdin.readline().rstrip())

cursor = 0
start = 0

while cursor < len(word):
    if word[cursor] == "<":       
        cursor += 1 
        while word[cursor] != ">":      
            cursor += 1 
        cursor += 1               
    elif word[cursor].isalnum(): 
        start = cursor
        while cursor < len(word) and word[cursor].isalnum():
            cursor+=1
        tmp = word[start:cursor] 
        tmp.reverse()       
        word[start:cursor] = tmp
    else:                   
        cursor+=1                

print("".join(word))