import sys
import heapq

input = sys.stdin.readline
INF = 1e9

def djk(start):
    distance = [INF] * (n + 1)
    que = []
    heapq.heappush(que,(0,start))
    distance[start] = 0

    while que:
        dist, now = heapq.heappop(que)


        if dist > distance[now]:
            continue

        for nxt, value in arr[now]:
            if distance[now] + value < distance[nxt]:
                distance[nxt] = distance[now] + value
                heapq.heappush(que,(distance[nxt], nxt))
    return distance

n,m = map(int,input().split())

arr = [[] for i in range(n+1)]


for i in range(m):
    s,e,v = map(int,input().split())
    arr[s].append((e,v))
    arr[e].append((s,v))

point1,point2 = map(int,input().split())

one_start = djk(1) # 1~n까지 최단거리
point1_start = djk(point1) # point1에서 n까지 최단거리
point2_start = djk(point2) # point2에서 n까지 최단거리

# 1 -> point1 -> point2 -> n
route1 = one_start[point1] + point1_start[point2] + point2_start[n]
# 1 -> point2 -> point1 -> n
route2 = one_start[point2] + point2_start[point1] + point1_start[n]

answer = min(route1, route2)

print(answer if answer<INF else -1) # answer가 INF이상이 되면 -1
