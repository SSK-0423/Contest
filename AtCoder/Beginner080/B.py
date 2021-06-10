n = int(input())
num = n
f = 0
while n > 0:
    f += n % 10
    n = n // 10

if(num % f == 0):
    print('Yes')
else:
    print('No')
