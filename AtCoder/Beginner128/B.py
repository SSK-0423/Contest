n = int(input())

p = [0]*100
store = []

for i in range(0,n):
    s,p[i] = map(str,input().split())
    store.append(s)

data = [store,p]

print(data)

sort_data = data.sort()
