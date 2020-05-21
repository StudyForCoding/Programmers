def solution(participant, completion):
    answer = ''
    val={}
    
    for i in participant:

        if i in val.keys():
            val[i]=val[i]+1
            
        else: 
            val[i]=1
    
    for i in completion:
        val[i]-=1
    
    for i in val.keys():
        if val[i]>0:
            answer=i
            break
    
    
    return answer