# 완전탐색적 사고

# 재료를 1부터 N까지 다 써보자
import sys
input = sys.stdin.readline

def recur(idx,dan,zzan,use):
    global answer

    if idx == n:
        if use == 0: # 아무 재료를 사용 안했다면
            return
        result = abs(dan-zzan)
        answer = min(answer,result)
        return

    # 재료 사용
    recur(idx+1,dan*ingre[idx][0],zzan+ingre[idx][1],use+1)

    # 재료 사용x
    recur(idx+1,dan,zzan,use)


n = int(input())
ingre = [list(map(int,input().split())) for _ in range(n)]

answer = float('inf')

recur(0,1,0,0) # 단 맛은 곱하기 1, 짠 맛은 더하기 0부터
print(answer)