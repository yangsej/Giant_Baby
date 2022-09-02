from collections import deque

def solution(queue1, queue2):
    answer = -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    N, M = len(q1), len(q2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    total = sum(q1) + sum(q2)
    if total % 2 == 0:
        half = total // 2
        
        for count in range((N+M) * 3):
            if sum1 < sum2:
                num = q2.popleft()
                q1.append(num)
                
                sum1 += num
                sum2 -= num
            elif sum1 > sum2:
                num = q1.popleft()
                q2.append(num)
                
                sum1 -= num
                sum2 += num
            else:
                answer = count
                break
                
    
#     queue = deque(queue1)
#     queue.extend(queue2)
    
#     N = len(queue)
#     if sum(queue) % 2 == 0:
#         sums = [0] * N
#         sums[0] = queue[0]
#         for i in range(N - 1):
#             sums[i+1] = sums[i] + queue[i+1]
        
#         subsum = 0
#         for i in range(N-1):
#             for j in range(i+1, N):
#                 subsum = sums[j] - sums[i]
#                 if subsum == sum(queue) // 2:
                    
            
            
        
    return answer
