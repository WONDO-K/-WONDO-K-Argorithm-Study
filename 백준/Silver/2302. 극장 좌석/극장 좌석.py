import sys
input = sys.stdin.readline


def solve(n, arr):

    dp = [0] * 41
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, 41):
        dp[i] = dp[i - 1] + dp[i - 2]

    prev = 0
    ans = 1

    for limit in arr: # vip 꺼냄
        ans *= dp[limit-1-prev] # limit(idx상 -1)에서 이전 위치를 뺀 값 = 해당 위치 까지의 갯수
        prev = limit # 어디까지 갯수를 카운트 했는지 저장

    ans *= dp[n-prev] # 마지막 vip 좌석 다음부터 끝 좌석까지

    return ans

n = int(input())
arr = []

for _ in range(int(input())):
    arr.append(int(input()))

print(solve(n,arr))