def solution(n, m):
    gcd, lcm = -1, n * m
    
    while m != 0:
        if n < m:
            n, m = m, n
        
        n, m = m, n % m
        
        gcd = n
        
    answer = [gcd, lcm // gcd]
    
    return answer
