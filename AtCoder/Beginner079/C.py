num = list(input())
ans = 7
for i in range(2 ** len(num)):
    total = 0
    ans_num = []
    ans_op = []
    for j in range(len(num)):
        if((i >> j) & 1):
            ans_num.append(num[j])
            if(j >= 1):
                ans_op.append('+')
            total += int(num[j])
        else:
            ans_num.append(num[j])
            if (j >= 1):
                ans_op.append('-')
            total -= int(num[j])
    if(total == ans):
        print(ans_num[0]+ans_op[0]+ans_num[1]+ans_op[1]+ans_num[2]+ans_op[2]+ans_num[3]+'=7')
        break