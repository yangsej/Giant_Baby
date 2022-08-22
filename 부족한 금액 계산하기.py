def solution(price, money, count):
    answer = -(money - price * (count * (count+1)) // 2)
    
    if answer < 0:
        answer = 0

    return answer
