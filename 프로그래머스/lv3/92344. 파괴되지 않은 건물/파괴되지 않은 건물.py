def solution(board, skill):
    answer = 0
    
    #공격 회복 결과 저장 그래프
    result = [[0]* (len(board[0])+1) for _ in range(len(board)+1)]
    
    for t, r1, c1, r2, c2, degree in skill :
        if t == 1 :
            result[r1][c1] -=degree
            result[r1][c2+1] +=degree
            result[r2+1][c1] +=degree
            result[r2+1][c2+1] -=degree
        else :
            result[r1][c1] +=degree
            result[r1][c2+1] -=degree
            result[r2+1][c1] -=degree
            result[r2+1][c2+1] +=degree
    
    for i in range (len(board)) :
        for j in range(len(board[0])) :
            result[i][j+1] +=result[i][j]
    
    for j in range (len(board[0])) :
        for i in range(len(board)) :
            result[i+1][j] +=result[i][j]
    
    
            
            
    for i in range (len(board)) :
        for j in range(len(board[0])) :
            if board[i][j] + result[i][j] > 0 :
                answer +=1
    
    
    return answer