n = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)
a = l[0]
if a < sum(l[1:]):
    print('Yes')
else:
    print('No')
