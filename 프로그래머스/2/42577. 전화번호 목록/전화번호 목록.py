def solution(phone_book):

    word_list = {}

    for i in phone_book:
        word_list[i] = 0

    for number in phone_book:
        for i in range(len(number)):

            if number[:i] in word_list:
                return False


    return True