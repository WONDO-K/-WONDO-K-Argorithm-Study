
def solution(array, target):
    result = []
    def recur(array, idx, sum_v):
        if idx == len(array):
            result.append(sum_v)
            return
        recur(array, idx + 1, sum_v + array[idx])
        recur(array, idx + 1, sum_v - array[idx])

    recur(array,0,0)
    cnt = result.count(target)
    return cnt

