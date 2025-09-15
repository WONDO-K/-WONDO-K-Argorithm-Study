def solution(genres, plays):
    answer = []
    dict1 = {} # 장르 별 총 재생 횟수
    dict2 = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in dict1:
            dict1[genre] = play
            dict2[genre] = [[i,play]]
        else:
            dict1[genre] += play
            dict2[genre].append([i,play])

    arr1 = sorted(dict1.items(), key = lambda x:x[1], reverse=True)

    for genre, total in arr1:
        arr2 = sorted(dict2[genre], key=lambda x: -x[1])
        cnt = 0
        for idx, play in arr2:
            if cnt >= 2:
                break
            answer.append(idx)
            cnt += 1

    return answer