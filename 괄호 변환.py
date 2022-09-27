def solution(p):
    answer = ''
    
    leftCount = 0
    rightCount = 0
    for i, c in enumerate(p):
        if c == '(':
            leftCount += 1
        else:
            rightCount += 1
        
        if leftCount > 0 and rightCount > 0 and leftCount == rightCount:
            u = p[:i+1]
            v = p[i+1:]
            
            count = 0
            for cu in u:
                if cu == '(':
                    count += 1
                else:
                    count -= 1
                    
                    if count < 0:
                        break
                        
            if count < 0:
                answer += '(' + solution(v) + ')'
                nu = list(u[1:-1])
                
                for j, cnu in enumerate(nu):
                    if cnu == '(':
                        nu[j] = ')'
                    else:
                        nu[j] = '('
                
                answer += ''.join(nu)
                    
            else:
                answer += u + solution(v)
            
            break
    
    return answer
