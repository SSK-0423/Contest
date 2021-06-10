a,b = map(int,input().split())

if(a >= 13):
    print(b,'\n')
elif(a >= 6 and a <= 12):
    print(b // 2,'\n')
else:
    print('0\n')
    