n = int(input())
a = list(map(int,input().split()))
flag = 0
count = 0

while(flag == 0):
    for j in range(0,n):
        if(a[j] % 2 != 0):
            flag = 1
            break
        else:
            a[j] = a[j] / 2
    if(flag == 1):
        break
    else:
        count = count + 1

print(count)
    
    
        
    