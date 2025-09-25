mod = {
    'a' : 5,
    'b' : 16,
    'c' : 20,
}

def check(arr,answers,student):
    cnt = 0
    
    for idx, answer in enumerate(answers):
        if answer == arr[idx%mod[student]]:
            cnt+=1
    return cnt

def solution(answers):
    answer = []
    
    a = [1,2,3,4,5]
    b = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5] # 16
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 20
    
    a_cnt = check(a,answers,'a')
    b_cnt = check(b,answers,'b')
    c_cnt = check(c,answers,'c')
    
    max_cnt = max(a_cnt, b_cnt, c_cnt)
    
    for idx,cnt in zip([1,2,3],[a_cnt,b_cnt,c_cnt]):
        if cnt == max_cnt:
            answer.append(idx)
    
    return sorted(answer)