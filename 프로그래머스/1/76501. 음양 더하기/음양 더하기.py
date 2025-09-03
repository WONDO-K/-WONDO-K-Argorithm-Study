def solution(absolutes, signs):
    answer = 0

    for ab, sig in zip(absolutes,signs):
        answer += ab if sig else -ab

    return answer