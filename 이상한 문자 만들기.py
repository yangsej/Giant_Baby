def solution(s):
    answer = ''
    
    count = 0
    for c in s:
        if c.isalpha():
            if count % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
                
            count += 1
        else:
            answer += c
            count = 0
            
    
    return answer
