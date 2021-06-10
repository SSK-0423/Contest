a,b,c,d = map(int,input().split())
count = 0
e = b - a
for i in range(a,d):
    if(i % c != 0 and i % d != 0):
        count += 1
        
for i in range(d,b + 1):
    if(i % c != 0 and i % d != 0):
        count += 1 
print(count)