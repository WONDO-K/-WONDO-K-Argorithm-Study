import sys
input = sys.stdin.readline

# 북, 동, 남, 서 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    cnt = 0

    while True:
        flag = False
        # 작업 1번
        if room_map[r][c] == 0:
            room_map[r][c] = 2
            cnt += 1

        # 작업 2로 갈지 3으로 갈지
        for i in range(4):
            nx = r+dx[i]
            ny = c+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if room_map[nx][ny] == 0: # 하나라도 청소할 칸이 있다면 작업 3번으로
                    flag = True
                    break
        # 작업 3번
        if flag:

            for i in range(4):
                d = (d+3) % 4 # 반시계 90도 회전 -> 시계방향 90도는 d=(d+1)%4
                nx = r+dx[d]
                ny = c+dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if room_map[nx][ny] == 0: # 작업 가능한 칸을 만나면 r,c를 갱신하고 반복문 중지 후 1번으로
                        r,c = nx,ny
                        break
        # 작업 2번 청소 가능한 칸이 없을 때
        else:
            r,c = r-dx[d],c-dy[d] # 1칸 후진
            if room_map[r][c]==1: #해당 칸이 벽(==1)이라면 스탑
                break

    return cnt

n,m = map(int,input().split())
r,c,d = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
print(get_count_of_departments_cleaned_by_robot_vacuum(r,c,d,arr))
