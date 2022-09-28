def solution(str1, str2):
    answer = 65536
    
    s1 = str1.lower()
    s2 = str2.lower()
    
    A = {}
    B = {}
    
    for i in range(len(s1)-1):
        if s1[i].isalpha() and s1[i+1].isalpha():
            if s1[i:i+2] not in A:
                A[s1[i:i+2]] = 0
            A[s1[i:i+2]] += 1
    
    for i in range(len(s2)-1):
        if s2[i].isalpha() and s2[i+1].isalpha():
            if s2[i:i+2] not in B:
                B[s2[i:i+2]] = 0
            B[s2[i:i+2]] += 1
            
    
    inter = 0
    union = 0
    for a in A:
        if a in B:
            inter += min(A[a], B[a])
            union += max(A[a], B[a])
        else:
            union += A[a]

    for b in B:
        if b not in A:
            union += B[b]
    
    if union:
        answer *= inter / union
        answer = int(answer)
    
    return answer
