from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def move(x,y,dir_x,dir_y):
    move_cnt = 0

    # 진행 방향으로 이동시 #이 아닐때 까지 and 도착지가 아닐때까지 이동
    while game_map[x+dir_x][y+dir_y] != '#' and game_map[x][y]!='O':
        x += dir_x
        y += dir_y
        move_cnt+=1
    return x,y,move_cnt

def is_available_to_take_out_only_red_marble(red_x, red_y, blue_x, blue_y ):
    # 구현해보세요!
    que = deque()

    # 빨간공 x,y 좌표, 파란공 x,y 좌표, 횟수
    que.append((red_x,red_y,blue_x,blue_y,1))
    visit[red_x][red_y][blue_x][blue_y] = True

    while que:
        rx,ry,bx,by,cnt = que.popleft()

        if cnt > 10: # 횟수 10회 초과시 실패 처리
            break

        for i in range(4):
            nrx, nry, r_cnt = move(rx,ry,dx[i],dy[i])
            nbx, nby, b_cnt = move(bx,by,dx[i],dy[i])

            if game_map[nbx][nby] == 'O': # 파란구슬이 구멍에 들어가면 실패 다음 경우로 넘어가야함
                continue
            if game_map[nrx][nry] == 'O':
                return cnt
            if nrx == nbx and nry == nby: # 현재 위치가 같은경우 이동거리가 많은 쪽이 늦게 도착한 경우
                if r_cnt>b_cnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = True
                que.append((nrx,nry,nbx,nby,cnt+1))
    return -1 # 10회 초과시 while문 탈출 및 -1 리턴

n,m = map(int,input().split())
red_x, red_y, blue_x, blue_y = 0,0,0,0
game_map = []

# rx,ry = (n,m)의 한칸 안에 bx,by(n,m)에 해당하는 2차원 배열이 들어있음 즉, 2^2 4차원 배열
visit = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    temp = list(input())
    game_map.append(temp)
    for j in range(m):
        if temp[j] == 'R':
            red_x,red_y = i,j
        elif temp[j]=='B':
            blue_x,blue_y = i,j

print(is_available_to_take_out_only_red_marble(red_x,red_y,blue_x,blue_y))  # True 를 반환해야 합니다

