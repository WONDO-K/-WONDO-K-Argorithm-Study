import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))
card.sort()
result={}

for i in card:
    if i not in result:
        result[i]=1
    else:
        result[i]+=1

m = int(input())
num = list(map(int,input().split()))

for i in num:
    left=0
    right=n-1
    while left<=right:
        mid = (left+right)//2

        if i == card[mid]:
            break
        if i < card[mid]:
            right = mid-1
        else:
            left = mid+1
    if i==card[mid]:
        print(result[i],end=' ')
    else:
        print(0,end=' ')