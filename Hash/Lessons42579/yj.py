def solution(genres, plays):
    code=dict()
    num=dict()
    for i in range(len(genres)):
        code[i]=(genres[i],plays[i])
        if genres[i] not in num.keys():
            num[genres[i]]=plays[i]
        else:
            num[genres[i]]+=plays[i]
            
    print(num)
    print(code)
    nums = sorted(num.items(), key =lambda x:x[1], reverse=True)
    codes = sorted(code.items(), key =lambda x:x[1], reverse=True)
    print(num)
    print(code)
    
    answer = []
    A=1
    for gen,_ in nums:
        for code,info in codes:
            if gen == info[0]:
                A+=1
                answer.append(code)
                if A>2:
                    A=1
                    break
                    
    return answer