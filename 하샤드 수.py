def solution(x):
    answer = x % sum(map(int, list(str(x)))) == 0
    
    return answer
