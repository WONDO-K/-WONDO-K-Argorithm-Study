from collections import Counter

def solution(X, Y):
    counter_x = Counter(X)
    counter_y = Counter(Y)

    common = []

    for num in range(10): # 0~9까지 숫자를 넣어보며 빈도수를 체크
        cnt = min(counter_x[str(num)],counter_y[str(num)]) # X와 Y중 num에 해당하는 숫자의 횟수가 작은 쪽을 선택
        common.extend([str(num)]*cnt) # 해당 숫자의 빈도수 만큼 common에 추가

    if not common: # 먼저 빈 배열을 걸러준다.
        return "-1"

		# 빈 배열은 위에서 걸렀으므로 제대로 0으로만 이루어진 배열이 도착하면 0 리턴
    if common.count("0") == len(common): # 전부 0으로 이루어져있으면
       return "0"

    return ''.join(sorted(common,reverse=True))
