n = int(input())

p = [0]*100
store = []

for i in range(0,n):
    s,p[i] = map(str,input().split())
    store.append(s)


num_data = dict(zip(p,list(range(0,n))))
num_data = dict((sorted(num_data.items())))

strd = dict(zip(store,list(range(0,n))))
strd = dict((sorted(strd.items())))

print(strd)



p = list(map(int,p))
print(p)

for i in range(0,n - 1):
    for j in range(i, n):
        if(store[i] == store[j]):
            if(p[i] < p[j]):
                box = p[i]
                p[i] = p[j]
                p[j] = box
            
print(p)


p_str = list(map(str,p))

for i in range(0,n):
    print(strd[p_str[i]] + 1)
    
         
