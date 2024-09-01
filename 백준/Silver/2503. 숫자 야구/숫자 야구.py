import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(str,input().split())) for _ in range(n)]


ans = 0

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):


            if (i==j or j==k or k==i):
                continue

            cnt = 0

            for target in arr:
                num = list(target[0])
                strike = int(target[1])
                ball = int(target[2])

                ball_cnt = 0
                strike_cnt = 0

                if (i == int(num[0])):
                    strike_cnt+=1
                if (j == int(num[1])):
                    strike_cnt+=1
                if(k == int(num[2])):
                    strike_cnt+=1

                if (i == int(num[1]) or i == int(num[2])):
                    ball_cnt+=1
                if (j == int(num[0]) or j == int(num[2])):
                    ball_cnt+=1
                if (k == int(num[0]) or k == int(num[1])):
                    ball_cnt+=1

                if (ball != ball_cnt):
                    break
                if (strike != strike_cnt):
                    break
                cnt+=1
            if cnt==n:
                ans+=1

print(ans)