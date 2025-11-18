import sys
input = sys.stdin.readline

N,C=map(int,input().split())
home = [int(input()) for _ in range(N)]
home.sort()
start=1
end=home[-1]-home[0]

result=0

while start<=end:
    mid = (start+end)//2
    point=home[0]
    count=1

    for i in range(1,len(home)):
        if home[i]>=point+mid:
            count+=1
            point=home[i]

    if count>=C:
        start=mid+1
        result=mid
    else:
        end = mid-1

print(result)