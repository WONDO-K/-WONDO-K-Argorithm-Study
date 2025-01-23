# 컴퓨터 수
n = int(input())
# 노드 수
m = int(input())

# 컴퓨터 연결 정보 배열
arr=[[] for _ in range(n+1)]

# 방문 기록
d_visit = [False for _ in range(n+1)]
b_visit = [False for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
# 컴퓨터 수를 셀 cnt
bfs_cnt=0

def bfs(x):
    global bfs_cnt

    b_visit[x] = True
    bfs_cnt+=1
    queue = [x]

    while queue:
        x = queue.pop()
        for nx in arr[x]:
            if b_visit[nx]==True:
                continue
            else:
                queue.append(nx)
                b_visit[nx]=True
                bfs_cnt+=1
bfs(1) 
print(bfs_cnt-1)