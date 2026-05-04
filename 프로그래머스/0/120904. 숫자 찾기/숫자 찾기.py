def solution(num, k):
    num_list = [int(i) for i in str(num)]
    
    for index, value in enumerate(num_list):
        if(value == k):
            return index + 1
        
    return -1