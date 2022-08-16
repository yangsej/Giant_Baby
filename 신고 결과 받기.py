# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []
    
    reports = {}
    counts = {}
    for user_id in id_list:
        reports[user_id] = set()
        counts[user_id] = 0
    
    for rep in report:
        plaintiff, defendant = rep.split()
        
        reports[defendant].add(plaintiff)
    
    for defendant in reports:
        if len(reports[defendant]) >= k:
            for plaintiff in reports[defendant]:
                counts[plaintiff] += 1
    
    for user in id_list:
        answer.append(counts[user])
    
    return answer
