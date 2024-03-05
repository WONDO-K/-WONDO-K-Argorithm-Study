import sys
input = sys.stdin.readline
inf = int(1e9)
n,m = map(int,input().split())

floor = [[inf for i in range(n)] for i in range(n)] 

for _ in range(m):
    a,b = map(int,input().split())
    floor[a-1][b-1] = 1
    floor[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                floor[i][j]=0
            else:
                floor[i][j] = min(floor[i][j],floor[i][k]+floor[k][j])

ans = []

for i in floor:
    ans.append(sum(i))
print(ans.index(min(ans))+1)
    