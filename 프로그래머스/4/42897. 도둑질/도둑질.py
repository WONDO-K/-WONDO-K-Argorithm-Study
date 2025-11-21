def solution(money):
    answer = []

    def get_max(start,end,dp):
        for i in range(start,end+1):
            dp[i] = max(dp[i-1],dp[i-2]+money[i])
        return dp[end]

    dp = [0] * len(money)
    dp[0] = money[0] # 0번 집을 털때는 dp가 0번 집의 돈을 가지고 시작해야함
    dp[1] = max(money[0],money[1]) 
    answer.append(get_max(0,len(money)-2,dp)) # 첫 집 텀
    dp = [0] * len(money)
    dp[1] = money[1] # 0번 집을 털지 않으므로  1번 집의 돈을 가지고 시작한다.
    dp[2] = max(money[1],money[2])
    answer.append(get_max(1,len(money)-1,dp)) # 첫 집 안텀

    return max(answer)


print(solution([1,2,3,1]))
print(solution([1,3,4,2,5]))