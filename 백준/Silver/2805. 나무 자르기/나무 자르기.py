import sys
input=sys.stdin.readline

n,m = map(int,input().split())

tree = list(map(int,input().split()))
tree.sort()

start,end = 1,tree[-1]
result = 0
while start<=end:
    mid = (start+end)//2
    cnt = 0
    for i in tree:
        if i>mid:
            cnt+= i-mid

    if cnt>=m:
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)