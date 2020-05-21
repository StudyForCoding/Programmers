def solution(phone_book):
    answer = True

    phones = dict()
    for one in phone_book:
        phones[one] = len(one)
    
    phones = sorted(phones.items(), key=lambda t : t[1])
    
    i = 0
    for phone in phones:
        for j in range(i + 1, len(phones)):
            if phone[0] == phones[j][0][0:phone[1]]:
                answer = False
                break
        if answer == False:
            break
        i += 1
    return answer