k,x = map(int,input().split())
ans = [i for i in range(x - (k - 1),x + (k - 1) + 1)]
for i in range(len(ans)):
    if i != len(ans) - 1:
        print(ans[i],'',end="")
    else:
        print(ans[i])