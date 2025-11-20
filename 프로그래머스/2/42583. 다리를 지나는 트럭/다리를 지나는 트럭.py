from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    que = deque([0]*bridge_length)
    truck_idx = 0
    total = 0
    while truck_idx < len(truck_weights) or total>0:
        answer+=1
        w = que.popleft()
        if w != 0:
            total-=w
        # while문의 조건이 or로 되어 있기 때문에 아직 다리 위에서 못빠져나간 트럭이 있다면 truck_idx가 이미 truck_weights를 초과하더라도 while문이
        # 계속해서 진행하기 떄문에 truck_idx가 계속 증가하여 index_error가 발생하기 떄문에 한번 더 확인해준 후에 무게 제한을 검사한다.
        if truck_idx < len(truck_weights) and total+truck_weights[truck_idx] <= weight: # 다리 위의 자동차 무게가 제한 무게 이내일 때
            que.append(truck_weights[truck_idx])
            total+=truck_weights[truck_idx]
            truck_idx+=1
        else: # 다리 위의 자동차 수가 다리 길이 보다 크거나 같을 때
            que.append(0)

    return answer