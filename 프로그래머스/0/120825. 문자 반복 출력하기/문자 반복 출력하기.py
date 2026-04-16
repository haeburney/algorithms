def solution(my_string, n):
    answer = ''
    stringList = list(my_string)
    
    for i in range(len(stringList)):
        answer += stringList[i] * n
    
    return answer