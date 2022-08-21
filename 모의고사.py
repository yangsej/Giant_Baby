def solution(answers):
    guess1 = [1, 2, 3, 4, 5]
    guess2 = [2, 1, 2, 3, 2, 4, 2, 5]
    guess3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == guess1[i%5]: scores[0] += 1
        if answers[i] == guess2[i%8]: scores[1] += 1
        if answers[i] == guess3[i%10]: scores[2] += 1

    answer = []
    max_score = max(scores)
    for i in range(len(scores)):
        if scores[i] == max_score:
            answer.append(i+1)
    
    return answer
