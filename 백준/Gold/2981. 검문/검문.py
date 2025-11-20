import sys, math
input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]
gaps = []

for i in range(1,n):
    gaps.append(abs(nums[i]-nums[i-1])) 

GCD = math.gcd(*gaps)
result = set() # 36의 약수 중 6,6 쌍이 생기는 데 이때는 중복이기 때문에 제거해줘야함 그래서 set을 사용

for i in range(2,int(GCD**0.5)+1): # GCD가 36이라면 6까지만 봐도 그 이후의 9, 12, 18, 36은 1,2,3,4,6으로 판별이 가능하다
    if GCD%i==0:
        # GCD가 36라면 36의 모든 약수는 1, 2, 3, 4, 6, 9, 12, 18, 36 가 될 것이고
        result.add(i) # i가 2일 때
        result.add(GCD//i) # 2의 짝인 18도 우리가 찾는 약수 중 하나기 때문에 저장해준다.
result.add(GCD)
print(*sorted(list(result)))
