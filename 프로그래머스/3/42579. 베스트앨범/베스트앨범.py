def solution(genre_array, play_array):

    dic = dict()
    result=[]
    
    for i in genre_array:
        dic[i] = [0,[]]

    for i in range(len(genre_array)):
        dic[genre_array[i]][0] += play_array[i]
        dic[genre_array[i]][1].append([i,play_array[i]])
        
    temp = sorted(dic.items(),key=lambda x:-x[1][0])
    
    for genre in temp:
        genre[1][1].sort(key=lambda x:(-x[1],x[0]))

    for genre in temp:
        if len(genre[1][1]) >= 2:
            result.append(genre[1][1][0][0])
            result.append(genre[1][1][1][0])
        else:
            result.append(genre[1][1][0][0])

    return result
