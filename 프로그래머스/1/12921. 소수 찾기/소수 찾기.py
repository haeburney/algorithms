def solution(n):
    decimal_number = []
    
    if(n < 2) : 
        return answer

    for i in range(2, n + 1):
        j = 1
        count = 0
        for num in decimal_number:
            if(num*num) > i :
                break
            if(i % num == 0):
                count += 1
                break
                
        if(count == 0):
            decimal_number.append(i)
    
    return len(decimal_number)