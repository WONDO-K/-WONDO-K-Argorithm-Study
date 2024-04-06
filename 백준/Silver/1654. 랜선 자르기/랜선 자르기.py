import sys
input=sys.stdin.readline

K,N = map(int,input().split())
lan=[int(input()) for _ in range(K)]
end=max(lan)

def devide_length(mid):
    count=0
    for i in lan:
        count += i//mid
    return count

def search(start,end,N):
    if start > end:
        return end
    mid = (start+end)//2
    length_count=devide_length(mid)
    if length_count>=N:
        return search(mid+1,end,N)
    else:
        return search(1,mid-1,N)

print(search(1,end,N))


