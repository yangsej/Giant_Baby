def solution(nums):
    answer = 0
    
    primes = [True] * 3001
    primes[0] = False
    primes[1] = False
    
    for i in range(2, 3001):
        if i * i > 3000:
            break
        
        for j in range(2, 3001):
            if i * j > 3000:
                break
            
            primes[i * j] = False
    
    
    N = len(nums)
    
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                num = nums[i] + nums[j] + nums[k]
                
                if primes[num]:
                    answer += 1
            

    return answer
