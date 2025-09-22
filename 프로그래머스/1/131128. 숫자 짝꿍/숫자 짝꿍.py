def solution(X, Y):
    answer=""
    hash_map = {}
    for y in Y:
        if y not in hash_map:
            hash_map[y] = 1
        else:
            hash_map[y]+=1

    for x in X:
        if x in hash_map:
            if hash_map[x] >0:
                hash_map[x]-=1
                answer+=x
    if answer.count("0") == len(answer):
        while '00' in answer:
            answer = answer.replace("00","0")

    answer = sorted(answer,reverse=True)

    return ''.join(answer) if len(answer)!=0 else "-1"