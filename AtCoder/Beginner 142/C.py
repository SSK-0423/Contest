import copy
N = int(input())
#A = list(map(int,input().split()))
A = list(range(0,100000))
B = copy.deepcopy(A)
B.sort()
num = [i for i in range(N)]
data = dict(zip(A,num))
ans = []
for i in B:
    ans.append(data[i]+1)
for i in ans:
    print(i,end=" ")