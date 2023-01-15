n = input()
n = int(n)
inp  = input()
li = inp.split()
xl = []
for i in li:
    k = int(i)
    xl.append(k)
cnt = 0
for i in range(1,n):
    if xl[i]<xl[i-1]:
        cnt += (xl[i-1] - xl[i])
        xl[i] = xl[i-1]
print(cnt)
