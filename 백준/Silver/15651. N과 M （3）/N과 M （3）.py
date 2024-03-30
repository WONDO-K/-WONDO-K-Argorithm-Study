
import sys
input=sys.stdin.readline

N,M = map(int,input().split())
result=[]


def recur(num):
    if num==M:
        print(' '.join(map(str,result)))
        return
    for i in range(1,N+1):
        result.append(i)
        recur(num+1)
        result.pop()
recur(0)