def solution(left, right):
    answer = sum(range(left, right+1))
    
    for i in range(right):
        if left <= i * i <= right:
            answer -= 2 * i * i
        
    
    return answer
