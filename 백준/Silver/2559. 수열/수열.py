import sys
input = sys.stdin.readline

n,k = map(int,input().split())

arr = list(map(int,input().split()))

result = []
end = len(arr)-(k)+1

for i in range(end):
    if len(result)==0:
        result.append(sum(arr[i:i+k]))
    else:
        result.append(result[i-1]-arr[i-1]+arr[i+k-1])
print(max(result))