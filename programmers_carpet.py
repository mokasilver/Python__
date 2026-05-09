#프로그래머스 탐색 - 카펫
def solution(brown, yellow):
    s = brown + yellow
    pairs = []
    answer = []
    for i in range(1, s+1):
        if (s%i) == 0:
            pairs.append(i)
    for i in range(0, len(pairs)):
        if pairs[i]>=s//pairs[i]:
            answer.append((pairs[i], s//pairs[i]))
            
            
    return answer[0]
