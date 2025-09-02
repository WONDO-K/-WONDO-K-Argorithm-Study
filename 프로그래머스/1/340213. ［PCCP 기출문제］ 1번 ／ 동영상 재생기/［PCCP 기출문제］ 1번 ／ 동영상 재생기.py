# 이걸 꼭 분과 초로 생각하지 말고 모두 초로 변환해서 풀면 더 쉽지 않을까?
# 04:05 -> 245
# 245 // 60 == 4
# 245 % 60 == 5
# 4분 5초

# 분 : 초 -> 초로 변환
def cal_to_sec(time):
    h,m = map(int,time.split(':'))
    return (h*60) + m
def trans_to_time(time):
    h = time // 60
    m = time % 60
    return_h = ''
    return_m = ''
    if h<10:
        return_h += "0"
        return_h += str(time // 60)
    else:
        return_h += str(time // 60)

    if m<10:
        return_m += '0'
    return_m += str(time % 60)

    return return_h + ":" + return_m


def solution(video_len, pos, op_start, op_end, commands):

    total_time = cal_to_sec(video_len)
    now_time = cal_to_sec(pos)
    op_start_time = cal_to_sec(op_start)
    op_end_time = cal_to_sec(op_end)


    for command in commands:
        if op_start_time <= now_time <= op_end_time:  # 오프닝 구간이면
            now_time = op_end_time
        # 이전 버튼
        if command == "prev":
            if now_time - 10 <= 0: #
                now_time=0
            else:
                now_time-=10

        # 다음 버튼 + 오프닝 건너뛰기
        else:
            if now_time+10>=total_time: # 10초를 넘기면 종료될때
                now_time = total_time
            else: # 종료되지 않으면
                now_time += 10
    if op_start_time <= now_time <= op_end_time:  # 오프닝 구간이면
        now_time = op_end_time
    return trans_to_time(now_time)

