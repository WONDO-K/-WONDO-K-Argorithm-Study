

def solution(tickets):
    answer = []
    tickets.sort()
    n = len(tickets)
    visit = [False]*n

    def dfs(path):
        if len(path) == n + 1:
            answer.append(path[:])
            return
        for i in range(n):
            if tickets[i][0]==path[-1] and not visit[i]:
                visit[i] = True
                path.append(tickets[i][1])
                dfs(path)
                path.pop()
                visit[i] = False



    dfs(['ICN'])
    return answer[0]
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	))