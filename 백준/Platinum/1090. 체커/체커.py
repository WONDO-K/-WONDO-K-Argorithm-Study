import sys

input = sys.stdin.readline

n = int(input())

arr = []

# a,b,c가 1,4,10 좌표에 있을 때 중간값인 5로 모이는 것 보다 중간에 위치한 b로 모이는 것이 가장 이득임
# 즉, 2차원 배열중 입력 받은 좌표 범위에 속해있는 위치들만 모두 확인하면 됨

# 이동거리를 계산하기 위해 x,y를 따로 한번 더 저장해준다.
arr_x = []
arr_y = []

ans = [-1]*n

for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])
    arr_x.append(a)
    arr_y.append(b)

    # 모이는 지점 x,y
    for y in arr_y:
        for x in arr_x:
            dist = []

            # 거리 비용 현재 좌표에서 목표 좌표 x,y를 빼주면 이동거리 나옴
            for now_x,now_y in arr:
                cost = abs(now_x-x) + abs(now_y-y)
                dist.append(cost)

            dist.sort()
            temp=0 # 이동거리 누적값 저장 용도

            for i in range(len(dist)): # dist는 0,1,2,3 ... 순으로 길이가 증가할 것임 0일 땐 0번째만, 1일때는 0,1번째 두개 누적
                distance = dist[i]
                temp+=distance

                if ans[i] == -1: # 초기상태란 의미
                    ans[i] = temp
                else: # 갱신이 된 값이라면
                    ans[i] = min(ans[i],temp) # ans에 있는 값과 현재까지 계산된 이동거리 중 작은 값 적용


print(*ans)