from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    que = deque()
    que.append((0,0,1))
    while que:
        x,y,cnt = que.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m: # 범위 초과하지  않고
                if maps[nx][ny] == 1: # 아직 방문하지 않았다면
                    maps[nx][ny] = cnt
                    que.append((nx,ny,cnt+1))
                    maps[x][y] = 0 # 현재 위치 벽으로 만들어줘야 역행 안함
    return -1