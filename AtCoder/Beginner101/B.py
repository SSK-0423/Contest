n = int(input())
m = n
sn = 0
while n:
    sn += n % 10
    n = n // 10

if m % sn == 0:
    print('Yes')
else:
    print('No')