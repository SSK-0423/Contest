n = int(input())
y = int(input())

baisu = y // 1000

a_num = a * 10
b_num = b * 5
c_num = c

count = 0

for i in range(0,a_num + 1,1000):
    for j in range(0,b_num + 1,500):
        num = baisu - (i + j)
        if(num >= 0 and num <= c_num):
            print(i,j,num)
            flag = 1
            break
        
    if(flag == 1):
        break
    
if(flag == 0):
    print('-1 -1 -1')