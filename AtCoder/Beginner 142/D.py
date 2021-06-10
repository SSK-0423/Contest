A,B = map(int,input().split())
common = []
for i in range(1,min(A,B)+1):
    if(B % i == 0 & A % i == 0):
        common.append(i)
print(common)