L,R = map(int,input().split())
ans = []
if(R - L >= 2019):
    print(0)
else:
    for i in range(L,R):
        for j in range(i+1,R+1):
            ans.append((i*j)%2019)
    print(min(ans))
     