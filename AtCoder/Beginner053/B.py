s = input()
numA = 0
for i in range(len(s)):
    if s[i] == 'A':
        numA = i + 1
        break

numZ = 0
for i in range(len(s)-1,-1,-1):
    if s[i] == 'Z':
        numZ = i + 1
        break
print(numZ - numA + 1)