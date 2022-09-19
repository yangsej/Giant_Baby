def solution(rows, columns, queries):
    N = len(queries)
    
    answer = [rows * columns] * N
    
    mat = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]

    for i, (x1, y1, x2, y2) in enumerate(queries):
        tmp = mat[x1-1][y2-1]
        
        for y in range(y2-1, y1-1, -1):
            mat[x1-1][y] = mat[x1-1][y-1]
            answer[i] = min(answer[i], mat[x1-1][y-1])
            
        for x in range(x1-1, x2-1):
            mat[x][y1-1] = mat[x+1][y1-1]
            answer[i] = min(answer[i], mat[x+1][y1-1])
            
        for y in range(y1-1, y2-1):
            mat[x2-1][y] = mat[x2-1][y+1]
            answer[i] = min(answer[i], mat[x2-1][y+1])
            
        for x in range(x2-1, x1-1, -1):
            mat[x][y2-1] = mat[x-1][y2-1]
            answer[i] = min(answer[i], mat[x-1][y2-1])
        
        mat[x1][y2-1] = tmp
        answer[i] = min(answer[i], tmp)
    
    return answer
