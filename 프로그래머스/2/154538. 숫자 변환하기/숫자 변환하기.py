from collections import deque

def solution(x,y,n):

    visit = set()
    que = deque()
    que.append((x,0))
    visit.add(x)
    while que:
        num,cnt = que.popleft()

        if num == y:
            return cnt

        for nxt in [num+n,num*2,num*3]:
            if nxt <= y and nxt not in visit:
                que.append((nxt,cnt+1))
                visit.add(nxt)

    return -1