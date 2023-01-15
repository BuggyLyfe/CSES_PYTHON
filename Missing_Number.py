n = input()
n = int(n)
x = input()
li = x.split()
pr = []
for i in range(n+1):
    pr.append(True)
for i in li:
    k=int(i)
    pr[k]=False
for i in range(1,n+1):
    if pr[i]==True:
        print(i)
        break
