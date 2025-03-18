def solution(string):
    
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if len(stack)==0:
                return False
            if stack[-1] == "(":
                stack.pop()
    if len(stack) == 0:
        return True
    return False
