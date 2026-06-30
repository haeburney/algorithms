from functools import cmp_to_key

def solution(numbers):
    def compare(a, b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        if ab > ba:
            return -1  
        elif ab < ba:
            return 1
        else:
            return 0

    numbers.sort(key=cmp_to_key(compare))
    
    answer = ''
    
    for value in numbers: 
        answer = answer + str(value)
        
    if answer[0] == '0':
        return '0'
    
    return answer