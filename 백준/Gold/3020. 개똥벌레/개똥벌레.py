import sys
input = sys.stdin.readline
n,h = map(int,input().split())

line = [0 for _ in range(h)]

for i in range(n):
    height = int(input())

    if i%2 == 0:
        line[0]+=1
        line[height] -=1
    else:
        line[h-height] +=1

prefix = [0 for _ in range(h+1)]

for i in range(h):
    prefix[i+1] = prefix[i]+line[i]
prefix = prefix[1:]
print(min(prefix), prefix.count(min(prefix)))