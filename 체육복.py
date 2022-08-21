def solution(n, lost, reserve):
    answer = n
    
    counts = [1] * (n+2)
    
    for l in lost:
        counts[l] -= 1
    
    for r in reserve:
        counts[r] += 1
    
    for i in range(1, n+1):
        if counts[i] == 0:
            if counts[i-1] > 1:
                counts[i-1] -= 1
                counts[i] += 1
            elif counts[i+1] > 1:
                counts[i+1] -= 1
                counts[i] += 1
    
    for i in range(1, n+1):
        if counts[i] == 0:
            answer -= 1
    
    return answer
