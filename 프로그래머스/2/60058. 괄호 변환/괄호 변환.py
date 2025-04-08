def check_correct(arr):
    stack = []

    if arr[0] == ")" or arr[-1]!=")":
        return False

    for i in arr:
        if i == "(":
            stack.append(i)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return True

def divide_arr(arr):
    n = len(arr)
    open_cnt, close_cnt = 0, 0
    u, v = "", ""
    for i in range(0,n):
        if arr[i] == "(":
            open_cnt+=1
        elif arr[i] == ")":
            close_cnt+=1

        if open_cnt == close_cnt:
            if open_cnt != 0 and close_cnt!=0:
                u += arr[0:i+1]
                if i != n:
                    v += arr[i+1:n]
                break
    return u,v

def solution(arr):
    n = len(arr)

    if len(arr) == 0 : # 빈 문자열이거나 이미 올바른 괄호
        return ""

    u,v = divide_arr(arr)
    if check_correct(u): # 3-1
        return u+solution(v) # 3-2
    else:

        temp = ""
        for i in u[1:-1]:
            temp += ")" if i == "(" else "("
        return "("+solution(v)+")"+temp
