def solution(participant, completion):
    answer = ''
    
    dic = dict()
    for p in participant:
        dic[p] = 0
    for p in participant:
        dic[p] += 1
    for c in completion:
        dic[c] -= 1
    for p in participant:
        if dic[p] == 1:
            answer = p
            break
    return answer