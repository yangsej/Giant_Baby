def solution(s, n):
    answer = ''
    
    for c in s:
        if c.isalpha():
            base = 'a'
            if c.isupper():
                base = 'A'
            answer += chr((ord(c) - ord(base) + n) % 26 + ord(base))
        else:
            answer += c
    
    return answer
