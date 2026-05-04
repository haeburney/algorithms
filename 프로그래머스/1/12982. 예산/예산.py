def solution(d, budget):
    d.sort()
    answer = 0 
    
    for value in d:
        if budget - value < 0:
            break
        budget -= value
        answer += 1
        
    return answer