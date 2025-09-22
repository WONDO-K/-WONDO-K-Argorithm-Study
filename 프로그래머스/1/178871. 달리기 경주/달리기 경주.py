def solution(players, callings):

    hash_map = {}

    for idx, player in enumerate(players):
        hash_map[player] = idx

    for call in callings:
        idx = hash_map[call]

        # 딕셔너리의 idx 값 바꾸기 -> 이 작업이 먼저와야 하는 이유 : players의 위치를 바꾼후에는 player[idx-1]값이 변질되어 버림
        # idx = 현재 호명한 추월 선수의 위치 -> 추월당한 선수의 위치로 바뀜
        hash_map[call] -=1 # 추월한 선수
        hash_map[players[idx-1]] +=1 # 추월당한 선수

        players[idx],players[idx-1] = players[idx-1],players[idx] # players의 위치 바꾸기


    return players