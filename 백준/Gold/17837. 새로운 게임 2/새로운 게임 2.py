
# 동 서 북 남
# 0, 1, 2, 3
# →, ←, ↑, ↓
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def change_direc(game_map,horse_map,horse_idx,y,x,d):
    # 다음에 이동할 좌표 값
    ny,nx = y+dy[d], x+dx[d]
    # 현재 좌표에 쌓여 있는 말들
    stack = horse_map[y][x]
    # 현재 이동해야할 말의 번호의 위치 값
    idx = stack.index(horse_idx)
    # 스택에서 현재 이동해야할 말과 그 위로 쌓인 말들 슬라이싱(이동해야할 말들)
    moving = stack[idx:]
    # 이동할 말들을 제외하고 남는 말들만 남겨 horse_map을 인덱스 아래에 위치한 말들만 슬라이싱
    # horse_map[y][x] = stack[:idx]

    # 방향 정보 변경하기
    def reverse_direc(d):
        # 짝수면 d+1, 홀수면 d-1을 하면 현재 방향의 반대 방향 구할 수 있음
        return d + 1 if d % 2 == 0 else d - 1

    # 범위를 벗어나거나 파란색 타일일 경우
    if not (0<=ny<n and 0<=nx<n) or game_map[ny][nx] ==2:
        new_d = reverse_direc(d)
        start_horse_location_and_directions[horse_idx][2] = new_d
        ny,nx = y+dy[new_d], x+dx[new_d]
        if not (0 <= ny < n and 0 <= nx < n) or game_map[ny][nx] == 2: # 또다시 파란색이거나 벗어나는 경우
            # 움직이지 않고 종료
            return y,x,new_d

    if game_map[ny][nx] == 1: # 빨간색
        moving = list(reversed(moving))

    horse_map[ny][nx].extend(moving)  # moving의 각 원소들을 순서를 뒤집어 extend로 하나씩 밀어 넣음
    horse_map[y][x] = stack[:idx]

    for moved_horse_idx in moving:
        start_horse_location_and_directions[moved_horse_idx][0] = ny
        start_horse_location_and_directions[moved_horse_idx][1] = nx

    return ny,nx,d


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    cnt = 1

    horse_map = [[[] for i in range(n)] for j in range(n)]
    for i in range(horse_count):
        y,x,d = horse_location_and_directions[i]
        horse_map[y][x].append(i)
    while cnt<=1000:
        for horse_idx in range(horse_count):
            y,x,d = horse_location_and_directions[horse_idx]
            ny,nx,nd = change_direc(game_map,horse_map,horse_idx,y,x,d)
            if len(horse_map[ny][nx]) >= 4:
                return cnt
        cnt += 1
    return -1

n,k = map(int,input().split())
chess_map = []
start_horse_location_and_directions = []
for i in range(n):
    chess_map.append(list(map(int,input().split())))

for i in range(k):
    y, x, d = map(int, input().split())
    start_horse_location_and_directions.append([y - 1, x - 1, d - 1])
print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))