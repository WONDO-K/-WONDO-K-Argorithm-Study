def solution(x):
    answer = True
    
    y = list(str(x))
    
    sum_v = sum(int(i) for i in y )
    
    return answer if x%sum_v == 0 else False
