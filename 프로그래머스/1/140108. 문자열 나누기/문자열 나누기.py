def solution(s):
    left, right = 0,0
    yes,no = 0,0
    result=[]
    while left<=right and right<len(s):
        if s[left] == s[right]:
            yes+=1
            right+=1
        elif s[left]!=s[right]:
            no+=1
            right+=1
        if yes==no:
            result.append(s[left:right])
            left = right
            right = left


    if left!=right:
        result.append(s[right-1])
    return len(result)