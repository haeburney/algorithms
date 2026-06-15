def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    return fatigability(k, visited, dungeons)

def fatigability(k, visited, dungeons):
    max_cnt = 0
    
    for idx, is_visit in enumerate(visited):
        if (not is_visit and k >= dungeons[idx][0]): # 방문 가능 & 던전에 갈 수 있는 체력
            visited[idx] = True 
            
            # 다음 던전 탐색
            cnt = 1 + fatigability(k - dungeons[idx][1], visited, dungeons)
            visited[idx] = False
            
            # 많이 방문한 곳 방문 
            max_cnt = max(max_cnt, cnt)
    
    return max_cnt