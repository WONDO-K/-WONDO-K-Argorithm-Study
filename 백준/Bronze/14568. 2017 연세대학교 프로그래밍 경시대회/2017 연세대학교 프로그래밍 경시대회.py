import sys

input = sys.stdin.readline

candy = int(input())
cnt=0
for a in range(1,candy+1):
    for b in range(1,candy+1):
        for c in range(1,candy+1):
            if a+b+c == candy:
                if a>=b+2:
                    if c%2==0:
                        cnt+=1

print(cnt)
