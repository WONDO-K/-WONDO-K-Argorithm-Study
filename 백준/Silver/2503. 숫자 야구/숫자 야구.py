import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
per = list(permutations([i for i in range(1,10)],3))

for _ in range(n):
    num,s,b = map(int,input().split())
    num = list(map(int,str(num)))
    temp=[]
    for target in per:
        score = [0, 0]
        for i, check in enumerate(num):
            if target[i] == check:
                score[0]+=1
            else:
                if check in target:
                    score[1]+=1
        if s == score[0] and b == score[1]:
            temp.append(target)
    per = temp

print(len(per))