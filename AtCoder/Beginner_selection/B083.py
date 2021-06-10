n,a,b = map(int,input().split())

total = 0

def sumdigits(i):
    i_sum = 0
    while(i > 0):
        i_sum += i % 10
        i = i // 10
        
    return i_sum

for j in range(1,n+1):
    num = sumdigits(j)
    if(num >= a and num <= b):
        total += j
    
print(total)
    


