def solution(s):
    answer = True
    
    count = 0
    for c in s:
        if c == '(':
            count += 1
        else:
            if count <= 0:
                answer = False
                break
            count -= 1
    
    if count != 0:
        answer = False

    return answer
