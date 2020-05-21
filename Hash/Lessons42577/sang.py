def solution(phone_book):
    for i in range(0, len(phone_book)):
        for j in range(0, len(phone_book)):
            if phone_book[i] == phone_book[j][0:len(phone_book[i])] and i != j:
                return False
    return True
