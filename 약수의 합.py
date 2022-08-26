def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        if i * i > n:
            break
        if (n // i) * i == n:
            if n//i == i:
                answer += i
            else:
                answer += i + n // i
    
    return answer
