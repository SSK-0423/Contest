N = int(input())
ans = []
depth = 1
def add_s(s,c,N,depth,s_list):
    if N == 1:
        for i in s:
            print(i)
        return
    
    if depth >= 2:
        s = [s + c]
        if len(s[0]) == N and not s in s_list:
            s_list.append(s[0])
            print(s[0])
    if depth == N:
        return s
    for i in s:
        add_s(i,'a',N,depth+1,s_list)
        add_s(i,'b',N,depth+1,s_list)
        add_s(i,'c',N,depth+1,s_list)

s = ['a','b','c']
add_s(s,'',N,depth,ans)