import sys
input = sys.stdin.readline

def merge_sort(start,end):
    global result

    if end-start<1:
        return
    
    m = (start + end)//2

    merge_sort(start,m)
    merge_sort(m+1,end)

    for i in range(start,end+1):
        temp[i] = a[i]

    k = start # 들어갈 배열의 위치를 의미한다.
    index1 = start
    index2 = m+1

    while index1 <= m and index2 <= end:
        if temp[index1]>temp[index2]:
            a[k] = temp[index2]
            result = result + index2 - k # swap 값을 카운트
            k+=1
            index2+=1
        else:
            a[k] = temp[index1]
            k+=1
            index1+=1
    while index1 <= m:
        a[k] = temp[index1]
        k+=1
        index1+=1
    while index2 <= end:
        a[k] = temp[index2]
        k+=1
        index2+=1


n = int(input())
a = list(map(int,input().split()))
result = 0
a.insert(0,0) # 0번째 인덱스를 넣어줌.
temp=[0]*(n+1)

merge_sort(1,n)

print(result)
