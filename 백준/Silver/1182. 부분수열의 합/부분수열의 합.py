import sys
input = sys.stdin.readline

n,s = map(int,input().split())
arr=list(map(int,input().split()))
cnt=0
def solve(idx,sum):
    global cnt

    if idx>=n:
        return

    sum+=arr[idx]

    if sum==s:
        cnt+=1
    # 현재 idx를 더하는 경우
    solve(idx+1,sum)
    # 현재 idx를 더하지 않는 경우
    solve(idx+1,sum-arr[idx])
    
solve(0,0)
print(cnt)