def solution(citations):
    answer = 0

    citations.sort()
    n = len(citations)
    left,right = 0,n

    while left<=right:
        mid = (left+right)//2
        cnt = 0
        for i in citations:
            if i >= mid:
                cnt+=1
        if cnt >= mid:
            left = mid+1
            answer=mid
        else:
            right = mid-1
    return answer