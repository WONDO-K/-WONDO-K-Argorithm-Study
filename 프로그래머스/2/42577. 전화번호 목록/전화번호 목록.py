def solution(phone_book):

    temp = {}

    for i in phone_book:
        temp[i] = 0
    for number in phone_book:
        for i in range(len(number)):
            if number[:i] in temp:
                return False
    return True
