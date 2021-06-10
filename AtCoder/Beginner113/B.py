n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))
ans_temp = 10**5
ans = 0
for i in range(n):
    temp = t - h[i] * 0.006
    if abs(a - ans_temp) > abs(a - temp):
        ans_temp = temp
        ans = i
print(ans + 1)