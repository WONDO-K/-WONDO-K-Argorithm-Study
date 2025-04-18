import sys,heapq
input = sys.stdin.readline
INF = int(1e9)

def sol(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                graph2[i[0]]=now
                heapq.heappush(q,(cost,i[0]))

n = int(input())
m = int(input())

graph = [[]for i in range(n+1)]
distance = [INF]*(n+1)
graph2 = [0] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start,end = map(int,input().split())

sol(start)
print(distance[end])

result = []

while end:
    result.append(end)
    end = graph2[end]
print(len(result))
print(*result[::-1])