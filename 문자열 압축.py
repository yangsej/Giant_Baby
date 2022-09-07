def solution(s):
    answer = len(s) * 2
    
    if len(s) == 1:
        answer = 1
    else:
        for l in range(1, len(s) // 2 + 1):
            total = 0 # len(s) % l
            count = 1
            for i in range(0, len(s), l):
                if s[i:i+l] == s[i+l:i+2*l]:
                    count += 1
                else:
                    total += len(s[i:i+l])
                    if count > 1:
                        total += len(str(count))
                    count = 1

                # print(total, count, s[i:i+l], s[i+l:i+2*l])

            answer = min(answer, total)
                
    return answer
