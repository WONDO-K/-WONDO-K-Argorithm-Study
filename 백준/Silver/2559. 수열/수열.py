a,b = map(int, input().split())

tmp_a =  list(map(int, input().split()))
tmp_b = [0 for i in range(a+1)]
ans = []
for i in range(a):
    tmp_b[i+1] = tmp_b[i]+tmp_a[i]

for i in range(a-b+1):

    ans.append(tmp_b[i+b]-tmp_b[i])

print(max(ans))