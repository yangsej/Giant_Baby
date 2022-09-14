def dfs(arr, index, ret, target):
    if(index == len(arr)):
        if(ret == target): return 1
        else: return 0
    else:
        num = arr[index]
        count = 0
        count += dfs(arr, index+1, ret+num, target)
        count += dfs(arr, index+1, ret-num, target)
        return count

def solution(numbers, target):
    answer = 0
    
    answer += dfs(numbers, 0, 0, target)
    
    return answer
