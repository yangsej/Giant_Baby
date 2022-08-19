def solution(s):
    answer = 0
    
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for n in range(len(nums)):
        s = s.replace(nums[n], str(n))
    
    answer = int(s)
    
    return answer
