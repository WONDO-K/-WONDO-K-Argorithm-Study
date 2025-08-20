import sys
input = sys.stdin.readline

n = 1000-int(input())
cnt = 0
coin = [500,100,50,10,5,1]

for money in coin:
    cnt += n//money
    n %= money

print(cnt)
