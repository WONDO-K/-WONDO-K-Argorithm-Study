def solution(answers):
    result = []
    
    a = [1,2,3,4,5] # 5
    b = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5] # 16
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 20
    
    point = [0,0,0]
    
    # answers의 인덱스가 길어지면 길어질 수록 각 a,b,c의 인덱스를 넘어서는 경우가 발생하는데 
    # 이때 각 배열의 길이로 나눈 나머지를 인덱스로 하여 접근하면 다시 0번 인덱스에서 출발한다. 
    for idx, answer in enumerate(answers):
        if a[idx%len(a)] == answer:
            point[0]+=1
        if b[idx%len(b)] == answer:
            point[1]+=1
        if c[idx%len(c)] == answer:
            point[2]+=1
    
    max_cnt = max(point)
    
    for idx,cnt in enumerate(point):
        if cnt == max_cnt:
            result.append(idx+1)
    # 어차피 순서대로 돌면서 result에 append 하기 때문에 정렬이 필요없다.
    return result

