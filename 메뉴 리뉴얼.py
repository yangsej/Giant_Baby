from itertools import combinations

def solution(orders, course):
    answer = []
    
    for cnt in course:
        courseMap = {}
        for order in orders:
            for newCourse in list(map(''.join, map(sorted, combinations(order, cnt)))):
                if newCourse not in courseMap:
                    courseMap[newCourse] = 0
                courseMap[newCourse] += 1

        if not courseMap:
            continue
            
        maxCnt = max(courseMap.values())
        if maxCnt < 2:
            continue
            
        for newCourse in courseMap:
            if courseMap[newCourse] == maxCnt:
                answer.append(newCourse)
    
    answer.sort()
    
    return answer
