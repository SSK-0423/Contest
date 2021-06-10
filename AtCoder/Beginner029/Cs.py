def brute_forece(n,s):
    if n==0:
        print(s)
        return 0
    else:
        for i in ["a","b","c"]:
            brute_forece(n-1,s+i)
n=int(input())
brute_forece(n,"")