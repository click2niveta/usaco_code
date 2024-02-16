n = int(input())
s = input().strip()

segments = []

region = 0
for i in range(n):
    if s[i]=='1': region += 1
    else: 
        if region>0: segments.append(region)
if region>0: segments.append(region)

numInf = n
for window in range(1, n+1, 2):
    tempInf = 0
    for i in range(len(segments)):
        flag = False
        block = segments[i]
        if (i==0 and s[0]=='1') or (i==len(segments)-1 and s[n-1]=='1'):
            if (window > block*2-1):
                flag = True
                break
        else:
            if (window > block):
                flag = True
                break
        tempInf += (block+window-1)/window
    print(numInf)
    numInf = min(numInf,tempInf)

    if flag == True: 
        break

print(numInf)