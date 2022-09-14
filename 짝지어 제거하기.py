def solution(s):
    answer = 1

    stack = []
    
    for c in s:
        stack.append(c)
        
        while len(stack) >= 2:
            if stack[-2] == stack[-1]:
                stack.pop()
                stack.pop()
            else:
                break
    
    if stack:
        answer = 0
                    
    return answer
