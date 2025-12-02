from collections import deque

def solution(priorities, location):
    result = []
    que = deque(priorities)
    idx_que = deque([i for i in range(len(priorities))])

    while que:
        work = que.popleft()
        loc = idx_que.popleft()
        if len(que) == 0:
            result.append(loc)
            continue
        if work >= max(que):
            result.append(loc)
        else:
            que.append(work)
            idx_que.append(loc)

    return result.index(location)+1

print(solution([2, 1, 3, 2],2))
print(solution([1,1,9,1,1,1],0))