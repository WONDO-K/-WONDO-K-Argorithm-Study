import sys

input = sys.stdin.readline

# 집합을 합칠 때
# 같은 대표를 공유하는 모든 원소의 대표 번호를 변경해줘야함

def find(x):
    while parent[x]!=x:
        parent[x] = parent[parent[x]] # 6의 대표는 7 -> 7의 대표는 1 -> 6의 대표는 1로 초기화
        x = parent[x] # 가장 최상위 대표로 초기화된 x를 저장후 리턴
    return x

def union(a,b):
    ra,rb = find(a),find(b) # 대표자 번호를 가져옴
    if ra != rb: # 대표자 번호가 서로 다르다면 ex) 0,1,1 의 경우 a,b가 같아서 합쳐줄 필요가 없다.
        parent[rb] = ra # 대표자 번호를 한쪽으로 몰아준다.


n,m = map(int,input().split())

parent = [i for i in range(n+1)]


for _ in range(m):
    order,a,b = map(int,input().split())
    if order == 1:
         print("YES") if find(a)==find(b) else print("NO")
    else: # 집합 합치기
        union(a,b)


