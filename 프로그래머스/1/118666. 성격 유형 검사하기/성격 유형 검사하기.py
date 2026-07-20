def solution(survey, choices):
    answer = ''
    count = [0, 0, 0, 0, 0, 0, 0, 0]
    types = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    # R=0, T=1, C=2, F=3, J=4, M=5, A=6, N=7
    
    for i in range(len(survey)):
        input_type = list(survey[i])
        
        # 알파벳 순서 정렬 및 점수 역전
        if input_type[0] > input_type[1]:
            input_type.sort()
            choices[i] = 8 - choices[i]
            
        first_char = input_type[0]
        choice = choices[i]
        
        if first_char == 'R':
            if choice >= 4:
                count[1] += choice - 4
            else:
                count[0] += 4 - choice
        elif first_char == 'C':
            if choice >= 4:
                count[3] += choice - 4
            else:
                count[2] += 4 - choice
        elif first_char == 'J':
            if choice >= 4:
                count[5] += choice - 4
            else:
                count[4] += 4 - choice
        elif first_char == 'A':
            if choice >= 4:
                count[7] += choice - 4
            else:
                count[6] += 4 - choice

    # 점수 비교 후 결과 문자열 생성
    for i in range(4):
        if count[i * 2] >= count[i * 2 + 1]:
            answer += types[i * 2]
        else:
            answer += types[i * 2 + 1]
            
    return answer