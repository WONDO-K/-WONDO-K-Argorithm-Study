import sys
input = sys.stdin.readline

n = int(input())

l = []

for i in range(n):
    start,end = map(int,input().split())
    l.append([start,end])

l.sort(key = lambda x : (x[1], x[0]))

last = 0
cnt = 0

for i,j in l:
    if i>= last:
        cnt+=1
        last=j

print(cnt)