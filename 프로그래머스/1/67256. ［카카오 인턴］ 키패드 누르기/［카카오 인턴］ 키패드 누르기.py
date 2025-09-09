from collections import deque


dx = [-1,1,0,0]
dy = [0,0,-1,1]
key_pad = [[1,2,3], [4,5,6], [7,8,9], ['*', 0, "#"]]
idx_map = {
    1:0,
    2:1,
    3:2,
    4:0,
    5:1,
    6:2,
    7:0,
    8:1,
    9:2,
    0:1,
}

def bfs(x,y,target):

    visit = [[0]*3 for i in range(4)]

    result = 1e9
    result_x, result_y = 0,0
    que = deque()
    que.append((x,y,0))

    if key_pad[x][y] == target:
        return x,y,0

    while que:
        x,y,cnt = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<4 and 0<=ny<3 and not visit[nx][ny]:
                if key_pad[nx][ny] == target:  # 다음 갈 곳이 만약 찾아야하는 숫자라면
                   #print(f'target! x:{nx},y:{ny},value:{key_pad[nx][ny]}')
                    result = min(result, cnt+1)
                    result_x, result_y = nx, ny
                    continue
                que.append((nx,ny,cnt+1))
                visit[nx][ny]=1
                
    return result_x, result_y, result

def solution(numbers, hand):
    answer = ''

    left_hand = [3,0]
    right_hand = [3,2]

    for number in numbers:
        if idx_map[number] == 0:
            l_x,l_y,l_cnt = bfs(left_hand[0], left_hand[1], number)
            left_hand[0], left_hand[1] = l_x,l_y
            answer+='L'
        elif idx_map[number] == 2:
            r_x,r_y,r_cnt = bfs(right_hand[0], right_hand[1], number)
            right_hand[0], right_hand[1] = r_x,r_y
            answer += 'R'
        else:
            l_x, l_y, l_cnt = bfs(left_hand[0], left_hand[1], number)
            r_x, r_y, r_cnt = bfs(right_hand[0], right_hand[1], number)


            if l_cnt < r_cnt: # 왼손 이동거리가 짧을 때
                left_hand[0], left_hand[1] = l_x, l_y
                answer += 'L'
            elif l_cnt > r_cnt: # 오른손 이동거리가 짧을 때
                right_hand[0], right_hand[1] = r_x, r_y
                answer += 'R'
            else: # 같을 때
                if hand == "left":
                    left_hand[0], left_hand[1] = l_x, l_y
                    answer += 'L'
                else:
                    right_hand[0], right_hand[1] = r_x, r_y
                    answer += 'R'

    return answer