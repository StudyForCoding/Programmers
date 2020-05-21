def solution(phone_book):
    phone_book.sort()
    a = phone_book[0]
    for i in range(1,len(phone_book)):
        if a in phone_book[i]:
            return False
        else:
            return True