def solve(level,diffs,times,limit):
    total_time = 0

    for i in range(len(diffs)):
        if diffs[i] <= level:
            total_time+=times[i]
        else:
            total_time+=(times[i]+times[i-1])*(diffs[i]-level)+times[i]
        if total_time>limit:
            return False
    return True


def solution(diffs, times, limit):
    left,right = 1,max(diffs)
    answer = right
    while left<=right:
        mid = (left+right) // 2
        if solve(mid,diffs,times,limit):
            answer = mid
            right = mid-1
        else:
            left = mid+1

    return answer
