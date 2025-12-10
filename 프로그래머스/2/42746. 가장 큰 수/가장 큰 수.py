def solution(numbers):
    number = list(map(str,numbers))
    number.sort(key = lambda x:x*3, reverse=True)

    return str(int(''.join(number)))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0,0]))