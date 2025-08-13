import sys,heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra(start):

    que = []
    heapq.heappush(que,(0,start))
    dist[start] = 0

    while que:
        cnt, now = heapq.heappop(que)

        if cnt > dist[now]:
            continue

        for nxt in arr[now]:
            new_cnt = cnt + nxt[1]

            if new_cnt < dist[nxt[0]]:
                dist[nxt[0]] = new_cnt
                heapq.heappush(que,(new_cnt,nxt[0]))


n,d = map(int,input().split())
dist = [INF] * (d+1)
arr = [[] for _ in range(d+1)]

for i in range(d):
    arr[i].append((i+1,1))

for _ in range(n):
    s,e,w = map(int,input().split())
    if e>d:
        continue
    arr[s].append((e,w))

dijkstra(0)
print(dist[d])