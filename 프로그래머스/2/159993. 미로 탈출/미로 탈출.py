from collections import deque

# S : 시작지점
# E : 출구
# L : 레버
# O : 통로
# X : 벽


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start,end,maps):
    n, m = len(maps), len(maps[0])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    que = deque()

    flag = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                que.append((i,j,0))
                visit[i][j]=1
                flag=1
                break
        if flag: break

    while que:
        x, y, cnt = que.popleft()

        if maps[x][y] == end:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and maps[nx][ny] != "X":
                    visit[nx][ny] = 1
                    que.append((nx, ny, cnt + 1))
    return -1

def solution(maps):
    route1 = bfs('S','L',maps)
    route2 = bfs('L','E',maps)

    if route1 != -1 and route2 != -1:
        return route1+route2
    return -1