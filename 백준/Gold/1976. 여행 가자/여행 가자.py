import sys

input = sys.stdin.readline

def find(x):
    if parent[x] != x: 
        parent[x] = find(parent[x]) # 상위 노트로 초기화
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    parent[rb] = ra  # 또는 parent[ra] = rb 도 가능



n = int(input())
m = int(input())
parent = [i for i in range(n)]
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i,j)

goal = list(map(int,input().split()))


for point in goal:
    if find(point-1) != find(goal[0]-1):
        print("NO")
        exit()
print("YES")