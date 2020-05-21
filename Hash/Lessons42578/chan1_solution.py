import itertools

def solution(clothes):
    answer = 0
    a={}
    for i in clothes:
        if i[1] in a.keys():
            a[i[1]]+=1
        else:
            a[i[1]]=1        
    #사전형 구하기 완료

    answer=1
    for i in a.keys():
        answer=answer*(a[i]+1)
        
            
        
                   
    
    return answer-1
