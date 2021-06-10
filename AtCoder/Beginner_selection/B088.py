n = int(input())
a = list(map(int,input().split()))

alice = 0
bob = 0
count = 1

while(count <= n):
    alice += max(a)
    index = a.index(max(a))
    del a[index]
    count += 1
    
    if(len(a) > 0):
        bob += max(a)
        index = a.index(max(a))
        del a[index]
        count += 1
    
print(alice - bob)