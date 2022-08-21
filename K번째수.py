def solution(array, commands):
    answer = []
    for i, j, k in commands:
        array_part = array[i-1:j]
        array_part.sort()
        
        answer.append(array_part[k-1])
    
    return answer
