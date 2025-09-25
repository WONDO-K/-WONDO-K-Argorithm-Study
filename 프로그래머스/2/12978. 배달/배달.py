import heapq

def djk(start,graph,n):
    INF = int(1e9)
    dist = [INF] * (n+1)
    dist[start] = 0

    que = []
    heapq.heappush(que,(0,start))

    while que:
        now_dist, now_house = heapq.heappop(que)

        if now_dist > dist[now_house]:
            continue
        for nxt,cnt in graph[now_house]:
            cost = now_dist + cnt
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(que,(cost,nxt))
    return dist

def solution(N, road, K):
    answer = 0

    arr = [[] for i in range(N+1)]

    for temp in road:
        start,end,point = temp
        arr[start].append([end,point])
        arr[end].append([start,point])


    temp = djk(1,arr,N)

    for i in temp[1:]:
        if i<=K:
            answer+=1

    return answer


