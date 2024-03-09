from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().strip()
    n=int(input())
    error=0

    num=input().strip()
    que=deque(num[1:-1].split(','))

    if n==0:
        que=deque()

    r_cnt=0
    for i in p:
        if i == 'R':
            r_cnt+=1
        elif i == 'D':
            if len(que)==0:
                print("error")
                error+=1
                break
            else:
                if r_cnt%2==0:
                    que.popleft()
                else:
                    que.pop()

    if error==0:
        if r_cnt%2==0:
            print("["+",".join(que)+"]")
        else:
            que.reverse()
            print("["+",".join(que)+"]")