import sys
input = sys.stdin.readline


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    if len(fixed_seat_array) == total_count:
        return 1
    temp = []
    arr = list(range(1,total_count+1))

    start = 0
    for i in fixed_seat_array:
        temp.append(arr[start:i-1])
        start = i
    temp.append(arr[start:])

    ans = 1
    for i in temp:
        if len(i) != 0:
            ans = ans*dp[len(i)]

    return ans

total_count = int(input())

fixed_seat_array = []

for _ in range(int(input())):
    fixed_seat_array.append(int(input()))

dp = [0]*41
dp[1]=1
dp[2]=2

for i in range(3,41):
    dp[i] = dp[i-1]+dp[i-2]

print(get_all_ways_of_theater_seat(total_count,fixed_seat_array))