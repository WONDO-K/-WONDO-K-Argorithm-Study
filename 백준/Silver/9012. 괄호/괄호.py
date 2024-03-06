import sys

n=int(sys.stdin.readline())

for i in range(n):
    stack=[]
    a = sys.stdin.readline()

    for j in a:
        if j=='(':
            stack.append(j)
        elif j==')':
            if stack:
                stack.pop()
            else: #스택에 괄호가 없을 경우
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')