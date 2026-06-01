import math 
from collections import deque

def solution(progresses, speeds):
    # deque로 구현해보기
    days_queue = deque()
    
    # 작업일 정리
    for i in range(len(progresses)):
        days_queue.append(int(math.ceil((100 - progresses[i]) / speeds[i])))
    
    answer = []
    count = 1
    
    while(days_queue):
        peek = days_queue.popleft()
        count = 1
        
        while(days_queue and peek >= days_queue[0]):
            days_queue.popleft()
            count += 1     
        
        answer.append(count)
        
    return answer
