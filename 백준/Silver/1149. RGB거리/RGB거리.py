import sys
input = sys.stdin.readline

n = int(input())
color = [list(map(int,input().split())) for _ in range(n)]

for idx in range(1,n):
    color[idx][0] = min(color[idx-1][1],color[idx-1][2]) + color[idx][0]
    color[idx][1] = min(color[idx-1][0],color[idx-1][2]) + color[idx][1]
    color[idx][2] = min(color[idx-1][0],color[idx-1][1]) + color[idx][2]

print(min(color[-1]))
