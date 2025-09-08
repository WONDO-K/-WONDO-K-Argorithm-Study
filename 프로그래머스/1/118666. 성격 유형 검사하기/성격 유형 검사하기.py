score = [0,3,2,1,0,1,2,3]
check_list = [["R","T"], ["C","F"], ["J","M"], ["A","N"]]

def solution(survey, choices):
    test_type = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0
    }
    answer = ''

    # 각 지표에 대한 점수 계산
    for sur, choice in zip(survey,choices):
        if choice == 4:
            continue

        left, right = sur[0], sur[1]
        if choice < 4 :
            test_type[left]+=score[choice]
        else:
            test_type[right]+=score[choice]

    for left,right in check_list:
        if test_type[left] == test_type[right]:
            answer+= chr(min(ord(left),ord(right)))
        else:
            if test_type[left] > test_type[right]:
                answer+=left
            else:
                answer+=right
    return answer


