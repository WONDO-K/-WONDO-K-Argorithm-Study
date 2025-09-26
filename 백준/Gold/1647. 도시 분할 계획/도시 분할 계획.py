import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x: # 자기 자신과 루트 번호가 다를 경우
        parent[x] = find(parent[x]) # 부모의 부모 (최상위 루트)를 찾아 경로 압축
    return parent[x]

def union(a,b):
    ra,rb = find(a),find(b)
    if ra!=rb:
        if ra < rb:
            parent[rb] = ra
        else:
            parent[ra] = rb

def kruskal(n,graph):
    global parent
    parent = [i for i in range(n+1)]
    graph.sort(key=lambda x:x[2]) # 가중치 작은 순으로 정렬

    total = 0
    mst = []

    for s,e,w in graph:
        if find(s)!=find(e): # 서로 루트가 다르면 싸이클 x
            union(s,e)
            total+=w
            mst.append((s,e,w))

    max_edge = max(mst,key=lambda x:x[2]) # (6, 7, 4) 이런식으로 2번 인덱스(가중치)가 가장 높은 값을 가지고 있는 원소의 튜플을 리턴해준다.
    total-=max_edge[2] # 튜플 속 가중치를 전체 비용 total에서 빼주면 가장 비용이 많이 드는 노드를 제거한 결과가 나온다.

    return total




n,m = map(int,input().split())
edges = []
for _ in range(m):
    s,e,w = map(int,input().split())
    edges.append((s,e,w))

print(kruskal(n,edges))