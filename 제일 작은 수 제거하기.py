def solution(arr):
    answer = []
    
    arr.remove(min(arr))
    
    answer = arr if arr else [-1]
    
    return answer
