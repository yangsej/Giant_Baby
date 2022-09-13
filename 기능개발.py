import math

def solution(progresses, speeds):
    answer = []
    
    N = len(speeds)
    
    day = 0
    for i in range(N):
        pro = progresses[i]
        spd = speeds[i]
        
        curPro = pro + spd * day
        if curPro < 100:
            day += math.ceil((100 - curPro) / spd)
            answer.append(1)
        else:
            answer[-1] += 1
    
    return answer
