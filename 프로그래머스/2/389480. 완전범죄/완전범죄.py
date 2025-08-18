INF = 1e9

def solution(info, n, m):
    cnt = INF
    def dfs(idx, a_sum, b_sum):
        nonlocal cnt
        if a_sum >= n or b_sum >= m:  # 둘 중 하나라도 경찰에게 잡히면 가지치기
            return
        if a_sum >= cnt: # 이미 최소값보다 크거나 같아지면 가지치기
            return
        if a_sum>=history[idx][b_sum]: # dp에 저장된 a_sum보다 큰 값이라면 가지치기
            return
        history[idx][b_sum] = a_sum # 가지치기 당하지 않았따면 현재까지 최소값 a_sum 저장

        if idx == len(info): # 모든 물건에 대해서 탐색 했을 때
            cnt = min(cnt,a_sum)
            return

        dfs(idx+1,a_sum+info[idx][0],b_sum)
        dfs(idx+1,a_sum,b_sum+info[idx][1])

    # 각 칸은 idx번 물건까지 확인했을 때 b_sum인 경우 a_sum의 값이 저장되어 있음
    # m은 허용되지 않는 갯수이기 때문에 m-1까지만 있어도 되기 때문에 +1을 안해도 된다.
    history = [[INF]*m for _ in range(len(info)+1)]
    dfs(0,0,0)

    return -1 if cnt == INF else cnt

