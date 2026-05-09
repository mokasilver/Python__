#프로그래머스 탐색 - 모의고사 
def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    #맞힌 문제 개수 구하기 
    for i in range(len(answers)):
        answer = answers[i] 
        
        if answer == p1[i % len(p1)]:
            scores[0] += 1
        if answer == p2[i % len(p2)]:
            scores[1] += 1
        if answer == p3[i % len(p3)]:
            scores[2] += 1
            
    #최댓값 찾기    
    max_score = max(scores)
    result = []
    for i in range(len(scores)):
        if scores[i] == max_score:
            result.append(i + 1)
            
    return result
