def solution(genre_array, play_array):

    dic1 = dict() # 장르별 총 재생 수
    dic2 = dict() # 장르별 몇 번 인덱스에 몇 번의 재생 수를 가지고 있는가?
    result = []
    
    # 장르별 총 재생 수
    for i in range(len(genre_array)): # 딕셔너리는 기본적으로 키를 기준으로 검색하도록 설계됨-> dic1.keys()는 딕셔너리의 키 목록을 반환하는 불필요한 연산을 하게 된다.
        genre = genre_array[i]
        play = play_array[i]
        if genre not in dic1: # 키가 없을 때
            dic1[genre] = play
            dic2[genre] = [[i,play]]
        else: # 키가 있을 때
            dic1[genre] += play
            dic2[genre].append([i, play])


    # 장르별로 가장 재생 수가 많은 장르 중, 재생 수가 많은 순서대로
    arr1 = sorted(dic1.items(),key=lambda x:x[1],reverse=True)
    # 장르 내에서 가장 많은 재생 수 순서로 2곡을 넣는다.
    for genre, total in arr1:
        arr2 = sorted(dic2[genre],key=lambda x:-x[1])
        cnt=0
        for idx,play in arr2:
            if cnt>=2:
                break
            result.append(idx)
            cnt+=1
    return result
