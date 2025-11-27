import heapq

def solution(operations):

    max_heap = []
    min_heap = []
    visit = [0]*len(operations)
    idx = 0
    for opers in operations:
        oper = opers.split(" ")
        if oper[0] == 'I':
            heapq.heappush(max_heap,[-int(oper[1]),idx])
            heapq.heappush(min_heap,[int(oper[1]),idx])
            idx+=1
        else:
            if oper[1] == '1': # 최댓값 삭제
                while max_heap and visit[max_heap[0][1]]==1:
                    heapq.heappop(max_heap)
                if max_heap: # 최대힙이 비어있지 않다면
                    _, index = heapq.heappop(max_heap)
                    visit[index] = 1
            elif oper[1] == '-1': # 최솟값 삭제
                while min_heap and visit[min_heap[0][1]] == 1:
                    heapq.heappop(min_heap)
                if min_heap:  # 최대힙이 비어있지 않다면
                    _, index = heapq.heappop(min_heap)
                    visit[index] = 1


    # 최대값 최종 정리
    while max_heap and visit[max_heap[0][1]] == 1:
        heapq.heappop(max_heap)

    # 최소값 최종 정리
    while min_heap and visit[min_heap[0][1]] == 1:
        heapq.heappop(min_heap)


    if not max_heap or not min_heap:
        return [0, 0]

    return [-max_heap[0][0],min_heap[0][0]]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))