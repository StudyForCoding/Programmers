def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('')
    '''
    for i in completion:
        if i in participant:
            participant.remove(i)
    return participant[0]
    '''
    for i in range(len(participant)):
        if participant[i]!=completion[i]:
            return participant[i]