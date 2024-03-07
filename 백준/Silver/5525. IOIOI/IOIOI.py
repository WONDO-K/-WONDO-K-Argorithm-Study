import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

# Pn은 무조건 I부터 시작한다. index()를 통해 가장 먼저 등장하는 I의 위치부터 시작
start = s.index('I')
limit = (n+1)+n

pn = ''

for i in range(limit):
    if i%2==0:
        pn+='I'
    else:
        pn+='O'

cnt=0


for i in range(start,m-limit+1):
    # 첫 문자는 I로 시작해야하고 반드시 뒤에 O가 오기 때문에
    # I뒤에 O가 아닌 경우는 확인하지 않는다.
    if s[i]=='I' and s[i+1]=='O':
        if s[i:i+limit] == pn:
            cnt+=1

print(cnt)