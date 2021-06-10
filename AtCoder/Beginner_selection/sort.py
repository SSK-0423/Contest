a = [2, 7, 0, 20]

for i in range(0,len(a)):
    for j in range(0,len(a)):
        if(a[i] > a[j]):
            damp = a[i]
            a[i] = a[j]
            a[j] = damp
            
print(a)