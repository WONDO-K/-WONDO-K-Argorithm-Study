import sys, math
import heapq
input = sys.stdin.readline
INF = math.inf


def dijkstra(start):
    que = []
    heapq.heappush(que,(0,start))
    dist[start] = 0

    while que:
        cnt, now = heapq.heappop(que)

        if cnt > dist[now]: # 현재 뽑은 이동횟수가 저장된 이동횟수보다 크면 해당 경로 추가x(삭제)
            continue

        for nxt in maps[now]:
            nxt_cnt = nxt[1]+cnt # 1번 인덱스에 가중치 담겨있음 꺼내서 지금까지의 이동거리 cnt와 더함 -> 다음 노드까지 예상 이동거리

            if cnt < dist[nxt[0]]: # 현재 cnt가 다음 노드까지 최소거리보다 작다면 교체
                dist[nxt[0]] = nxt_cnt
                heapq.heappush(que,(nxt_cnt,nxt[0]))


n,m,k,x = map(int,input().split())
maps = [[] for i in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    s,e = map(int,input().split())
    # 종착지와 가중치(거리 - 이 문제에서 모두 거리는 1로 동일함)
    maps[s].append((e, 1))
dijkstra(x)

result = []

for i in range(1,n+1):
    if dist[i] == k:
        result.append(i)

if len(result)==0:
    print(-1)
else:
    for i in result:
        print(i)