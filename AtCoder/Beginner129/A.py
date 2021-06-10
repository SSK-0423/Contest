p,q,r = map(int,input().split())

mintime = p + q
if(mintime > p + r):
    mintime = p + r
elif(mintime > q + r):
    mintime = q + r

print(mintime)