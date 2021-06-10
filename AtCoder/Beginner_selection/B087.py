a = int(input())
b = int(input())
c = int(input())
x = int(input())

baisu = x // 50

a_num = a * 10
b_num = b * 2
c_num = c

count = 0

for i in range(0,a_num + 1,10):
    for j in range(0,b_num + 1,2):
        num = baisu - (i + j)
        if(num >= 0 and num <= c_num):
            count += 1


print(count)