import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 1이면 que에 넣는다.
n,m = map(int,input().split())
maps = []
history = []
time = 0
for i in range(n):
    maps.append(list(map(int,input().split())))

def sol():
    que = deque()
    que.append((0,0))
    visit[0][0] = True
    cnt = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
                if maps[nx][ny] == 0:
                    que.append((nx,ny))
                if maps[nx][ny] == 1:
                    maps[nx][ny]=0
                    cnt+=1 # 녹인 횟수
                visit[nx][ny] = True
    history.append(cnt)
    return cnt



while True:
    visit = [[False]*m for _ in range(n)]

    melt_cnt = sol()
    if melt_cnt == 0:
        print(time)
        print(history[-2])
        break
    time+=1