def solution(players, callings):

    hash_map = {}

    for idx, player in enumerate(players):
        hash_map[player] = idx

    for call in callings:
        idx = hash_map[call]

        players[idx],players[idx-1] = players[idx-1],players[idx] # players의 위치 바꾸기

        # 딕셔너리의 idx 값 바꾸기
        hash_map[players[idx]] = idx
        hash_map[players[idx-1]] = idx-1 # 추월한 선수의 위치가 추월당한 선수의 값으로 변경되었기 때문에

    return players