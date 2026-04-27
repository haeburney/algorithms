

def solution(n):
    decimal_number = [2]
    answer = 1
    
    if(n==2) : return answer

    for i in range(3, n + 1):
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