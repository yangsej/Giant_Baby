def solution(n):
    answer = ''
    
    NUMS = ['4', '1', '2']
    
    nums = []

    while n > 0:
        mod = n % 3
        n //= 3

        answer += NUMS[mod]
        
        if mod == 0:
            n -= 1
        
    
    answer = answer[::-1]
    
    return answer
