import sys
from collections import deque
input = sys.stdin.readline

def bfs(first_num,target):
    que = deque()
    que.append((first_num))
    visit[first_num]=1

    while que:
        idx= que.popleft()
        if idx == target:
            return visit[idx]-1

        for nxt in tree[idx]:
            if not visit[nxt]:
                visit[nxt] = visit[idx]+1
                que.append(nxt)
    return -1


a,b = map(int,input().split())
n,m = map(int,input().split())
visit = [0 for _ in range(n+1)]
tree = [[] for _ in range(n+1)]

for _ in range(m):
    start,end = map(int,input().split())
    tree[start].append(end)
    tree[end].append(start)



print(bfs(a,b))