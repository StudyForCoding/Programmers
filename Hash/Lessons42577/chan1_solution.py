def solution(phone_book):
    answer = True
    val={}
    for i in phone_book:
        val[i]=1
    
    for num in phone_book:
        temp=""
        for i in num:
            temp+=i
            if len(temp)==len(num):
                continue
            if temp in val:
                print(temp)
                return False
    
    
    return answer
