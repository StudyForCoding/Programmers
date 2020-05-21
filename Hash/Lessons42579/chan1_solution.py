def solution(genres, plays):
    answer = []
    a={}
    for i in range(len(genres)):
        
    #해시 형태 classic : {[500,0], [150,2] ,[800,3]}   
        
        temp={}
        temp[i]=plays[i]
        if genres[i] in a.keys():
            a[genres[i]].update(temp)   
        else:
            a[genres[i]]=temp
            
    #print(a)  
    #print(a.keys())  
    
    
    result_list=sorted(a.keys(),key=lambda x : sum([a[x][t] for t in a[x].keys()]), reverse=True)
    #print(result_list)
    for key in result_list:
        val_list=sorted(a[key].keys(),key=lambda x : (a[key][x],-x), reverse=True)
        #print(val_list)
        
        
        for num,val in enumerate(val_list):
            if num==2:
                break
            answer.append(val)

            
        
        
    return answer
