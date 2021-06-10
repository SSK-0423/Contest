n = int(input())
a = []
#入力
for i in range(0,n):
    a.append(int(input()))

num = []
#
while(len(a) > 0):
    
    num.append(max(a))
    index = max(a)
    
    for i in range(0,n):
        if(len(a) > 0 and index in a):
            a.remove(index)
            
print(len(num))
    