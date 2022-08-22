def solution(a, b):
    answer = ''
    
    DAY = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    answer = DAY[(sum(days[:a-1]) + b + 4) % 7]
    
    return answer
