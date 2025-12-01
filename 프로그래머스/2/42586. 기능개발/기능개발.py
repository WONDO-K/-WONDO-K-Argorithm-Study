from collections import deque

def solution(progresses, speeds):
    answer = []
    que = deque([])
    for work, speed in zip(progresses,speeds):
        day = (100 - work + speed-1)//speed
        que.append(day)
        
    prev = que.popleft()
    cnt = 1
    while que:
        day = que.popleft()
        if day > prev:
            answer.append(cnt)
            prev = day
            cnt=1
        else:
            cnt+=1
    answer.append(cnt)
    return answer



