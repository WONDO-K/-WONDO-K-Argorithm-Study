import heapq

def solution(n, s, a, b, fares):

    INF = int(1e9)
    answer = INF
    arr = [[] for _ in range(n + 1)]
    for x, y, w in fares:
        arr[x].append((y, w))
        arr[y].append((x, w))

    def djk(start):

        dist = [INF]*(n+1)
        dist[start]=0
        que = []
        heapq.heappush(que,(0,start))

        while que:
            now_dist, now_node = heapq.heappop(que)

            if now_dist > dist[now_node]:
                continue

            for next_node, weight in arr[now_node]:
                cost = now_dist + weight
                if cost < dist[next_node]: # 현재 거리가 이미 저장된 거리보다 작을 경우 갱신
                    dist[next_node] = cost
                    heapq.heappush(que,(cost,next_node))
        return dist


    dist_from_s = djk(s)
    dist_from_a = djk(a)
    dist_from_b = djk(b)

    for i in range(1, n+1):
        answer = min(answer,dist_from_s[i]+dist_from_a[i]+dist_from_b[i])

    return answer

