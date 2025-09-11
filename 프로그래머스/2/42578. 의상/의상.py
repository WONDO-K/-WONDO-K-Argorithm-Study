def solution(clothes):
    answer = 1

    hash_map = {}

    for _ ,i in clothes:
        if i in hash_map:
            hash_map[i] += 1 
        else:
            hash_map[i] = 1

    for i in hash_map:
        answer *= hash_map[i]+1

    return answer-1