a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0

for i in range(0,a):
    for j in range(0,b):
        for k in range(0,c):
            if(i * 500 + j * 100 + k * 50 == x):
                count += 1


print(count)