def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0);
    
    return answer

def dfs(numbers, target, index, currentCount):
    
    if(len(numbers) == index):
        if(currentCount == target):
            return 1
        else:
            return 0
    else:
        plus_result = dfs(numbers, target, index + 1, currentCount + numbers[index])
        minus_result = dfs(numbers, target, index + 1, currentCount - numbers[index])
        return plus_result + minus_result