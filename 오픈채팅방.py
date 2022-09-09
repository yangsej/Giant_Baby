def solution(record):
    answer = []
    
    users = {}
    for rec in record:
        r = rec.split()
        command, uid, user = r[0], r[1], r[2] if len(r) >= 3 else ""
        
        if command == "Enter":
            users[uid] = user
        elif command == "Change":
            users[uid] = user
        elif command == "Leave":
            pass
    
    for rec in record:
        r = rec.split()
        command, uid, user = r[0], r[1], r[2] if len(r) >= 3 else ""
        
        if command == "Enter":
            answer.append(users[uid] + "님이 들어왔습니다.")
        elif command == "Change":
            pass
        elif command == "Leave":
            answer.append(users[uid] + "님이 나갔습니다.")
        
    
    return answer
