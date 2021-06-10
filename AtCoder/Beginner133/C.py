L,R = map(int,input().split())
n = [i % 2019 for i in range(L,R+1)]
print(n)
i = n[n.index(min(n))]
n[n.index(min(n))] = 2020
j = n[n.index(min(n))]
print(i * j % 2019)