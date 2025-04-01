import heapq

def solution(string):
    if len(string) == 1:
        return 1
    ans = [] # 문자열 길이 최솟값 배출

    for cut in range(1,(len(string)//2) + 1): # 자르는 글자수가 n의 길이의 절반이 넘어가면 비효율적임
        num_cnt = []  # 글자의 갯수
        str_arr = []  # 문자열

        for idx in range(0,len(string),cut):
            temp = string[idx : idx+cut]
            if len(num_cnt) <= 0: # num_cnt가 0이라면 (현재 자른 글자와 갯수 1을 각각 배열에 추가) - ==0으로 해도 될듯, else 조건 확실히 하려고 이렇게 함
                num_cnt.append(1)
                str_arr.append(temp)
            else: # 이미 추가되어 있다면
                if str_arr[-1] == temp: # 현재 문자열이 이전 문자열과 같다면 숫자만 증가
                    num_cnt[-1]+=1
                else: # 현재 문자열이 이전 문자열과 다르다면 다시 갯수와 자른 문자열을 각 배열에 추가한다.
                    num_cnt.append(1)
                    str_arr.append(temp)

        temp = '' # 중복 제거한 문자열 저장
        for i in range(len(num_cnt)):
            if num_cnt[i] == 1: # 현재 순서의 중복수가 1이라면 문자열만 temp에 추가
                temp+=str_arr[i]
            else: # 현재순서의 중복수가 1이 아니라면 중복수를 문자열에 추가한 후 문자열도 추가한다.
                temp+=str(num_cnt[i])
                temp+=str_arr[i]
        heapq.heappush(ans,len(temp)) # heap에 완성된 temp의 길이를 추가
    return heapq.heappop(ans) # heap에서 최소값 꺼내기


