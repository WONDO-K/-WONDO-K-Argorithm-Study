import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = int(input())
    for i in range(2,1_000_001):
        if s % i  == 0: # 1 번이라도 나누어 떨어지면 100만 이하의 약수가 존재한다는 의미
            print('NO')
            break
        else:
            if i == 1_000_000: # 100만이하의 약수가 존재하지 않는다.
                print('YES')

