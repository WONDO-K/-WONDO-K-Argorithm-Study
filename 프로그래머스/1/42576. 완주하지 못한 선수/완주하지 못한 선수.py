def solution(participant, completion):

    hash_map = {}

    for name in completion:
        if name not in hash_map:
            hash_map[name] = 1
        else:
            hash_map[name] += 1

    for name in participant:
        if name not in hash_map:
            return name
        if hash_map[name] == 0:
            return name
        hash_map[name] -=1