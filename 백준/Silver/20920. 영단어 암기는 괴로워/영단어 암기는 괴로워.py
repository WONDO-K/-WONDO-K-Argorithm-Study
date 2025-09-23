import sys
input = sys.stdin.readline

n,m = map(int,input().split())
fruits = {}
for _ in range(n):
    fruit = input().rstrip()
    if len(fruit)>=m:
        if fruit not in fruits:
            fruits[fruit] = 1
        else:
            fruits[fruit]+=1

result = sorted(fruits.items(), key= lambda x:(-x[1],-len(x[0]),x[0]))

for key,value in result:
    print(key)