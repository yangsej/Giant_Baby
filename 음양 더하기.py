def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer += absolutes[i] * (1 if signs[i] else -1)
        
    return answer
