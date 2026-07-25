def solution(survey, choices):
    answer = ''
    
    type_scores = {
        "R": 0, "T": 0,
        "C": 0, "F": 0,
        "J": 0, "M": 0,
        "A": 0, "N": 0
    }
    
    for category, choice in zip(survey, choices):
        disagree_type = category[0]
        agree_type = category[1]
        
        if(choice >= 5):
            type_scores[agree_type] += choice - 4
        else :
            type_scores[disagree_type] += 4 - choice
            
    indicators = [("R", "T"), ("C","F"), ("J","M"), ("A","N")]
    
    for type_a, type_b in indicators:
        if(type_scores[type_a] >= type_scores[type_b]):
            answer += type_a
        else:
            answer += type_b
            
    return answer