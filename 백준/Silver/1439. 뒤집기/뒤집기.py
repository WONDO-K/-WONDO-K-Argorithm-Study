import sys
input = sys.stdin.readline

def find_count_to_turn_out_to_all_zero_or_all_one(string):

    cnt_zero, cnt_one = 0,0

    if string[0] == "0":
        cnt_one +=1
    else:
        cnt_zero+=1

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == "0":
                cnt_one += 1
            elif string[i+1] == "1":
                cnt_zero +=1
    return min(cnt_zero,cnt_one)

num = input()
result = find_count_to_turn_out_to_all_zero_or_all_one(num)
print(result)