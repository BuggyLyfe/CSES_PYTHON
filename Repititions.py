str = input()
cnt = 1
outp = 1
l = len(str)
for i in range(1,l):
    if str[i]==str[i-1]:
        cnt+=1
        if cnt>outp:
            outp = cnt
    else:
        cnt = 1
print(outp)
