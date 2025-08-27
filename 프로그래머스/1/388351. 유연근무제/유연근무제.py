# 시작하는 요일을 기준으로 일주일(7일)을 확인한다.
# 단, 주말의 기록은 영향을 주지 않는다. -> if 토 or 일 분기로 버리면 될듯
# 출근 시간은 출근 희망 시간 + 10분까지만 인정한다.

def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    histories = [[1,1,1,1,1,1,1] for _ in range(n)]
    
    for i in range(n): # i 번째 사원
        day = startday
        h = schedules[i] // 100
        m = schedules[i] % 100
        limit = schedules[i] + 10
        if m + 10 >= 60:
            limit = ((h + 1) * 100) + abs((60 - (m + 10)))

        for j in range(len(timelogs[0])): # i번째 사원의 근태기록
            if day == 8:
                day=1
            if day == 6 or day==7 : # 주말 제외
                day+=1
                continue
            if limit - timelogs[i][j] < 0: # 제한 시간에서 출근 시간 뺐을 때 음수면 지각한거임
                histories[i][j] = 0
                break # 한 번이라도 지각하면 이 직원은 상품 못받으니까 다른 요일 안봐도 된다.
            day+=1

    for history in histories:
        if 0 not in history:
            answer+=1
    return answer