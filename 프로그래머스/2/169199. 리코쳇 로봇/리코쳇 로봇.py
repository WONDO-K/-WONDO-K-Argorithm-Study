from collections import deque
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def solution(board):
    n,m = len(board),len(board[0])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    x,y = 0,0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                x,y=i,j
                break
        else:
            continue
        break

    que = deque()
    que.append((x,y,0))
    visit[x][y]=1
    while que:
        x,y,cnt = que.popleft()

        if board[x][y] == 'G':
            return cnt

        for i in range(4):
            nx,ny=x,y
            while 0<=nx<n and 0<=ny<m and board[nx][ny]!='D':
                nx+=dx[i]
                ny+=dy[i]
            # 벽을 넘거나, 장애물인 위치에서 멈추기 떄문에 한칸씩 뒤로 이동
            nx -= dx[i]
            ny -= dy[i]
            if not visit[nx][ny]:
                que.append((nx, ny, cnt + 1))
                visit[nx][ny] = 1
    return -1
