import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def recur(y,x): # dfs

    if dp[y][x]:
        return dp[y][x]
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<n:
            if arr[y][x] < arr[ny][nx]:
                dp[y][x] = max(dp[y][x], recur(ny,nx)+1)

    return dp[y][x] # 기본값0


n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
# 모든 점 방문
for y in range(n):
    for x in range(n):
        recur(y,x)

# 2차원 그래프에서 최대, 최소값 찾기
print(max(map(max,dp))+1)