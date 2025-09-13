def solution(nums):

    pocket = list(set(nums))
    limit = len((nums))//2

    if len(pocket)>= limit:
        return min(len(pocket),limit)
    else:
        return len(pocket)
