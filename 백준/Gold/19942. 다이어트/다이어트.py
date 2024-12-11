def recur(idx,p,f,c,v,price):
    global answer
    global used
    global answer_used

    if p >= protein and f >= fat and c >= carbo and v >= vitamin:
        if answer > price:
            answer = min(answer, price)
            answer_used = []
            for i in used:
                answer_used.append(i)            
    if idx == n:
        return
    
    used.append(idx+1)
    recur(idx+1, p+ing[idx][0], f +ing[idx][1], c + ing[idx][2], v + ing[idx][3], price+ing[idx][4])
    used.pop()

    recur(idx+1,p,f,c,v,price)

n = int(input())

protein, fat, carbo, vitamin = map(int,input().split())

ing = [[] for _ in range(n)]

for i in range(n):
    a,b,c,d,e = map(int,input().split())
    ing[i] = [a,b,c,d,e]

answer = 1e9

used = []
answer_used = []

recur(0,0,0,0,0,0)

answer_used.sort()

if answer_used:
    print(answer)
    print(*answer_used)
else:
    print(-1)
