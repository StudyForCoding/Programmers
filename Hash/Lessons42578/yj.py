def solution(clothes):
    style = dict()
    for i in clothes:
        if i[1] not in style:
            style[i[1]]=1
        else : 
            style[i[1]]+=1
    print(style)
    answer =1
    for i in style.values():
        answer*=(i+1)
    return answer-1