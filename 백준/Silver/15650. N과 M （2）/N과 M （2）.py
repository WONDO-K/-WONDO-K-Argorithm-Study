import sys

def recur(num):

    if len(arr) == m :
        print(*arr)
        return

    for i in range(num,n): # 현재 arr의 길이 즉, 현재 순번을 의미. 
        arr.append(nums[i])
        recur(i+1)
        arr.pop()

n,m = map(int,input().split())
arr = []
nums =[ i for i in range(1,n+1)]
recur(0)