n = int(input())
x = int((n*(n+1))/2)
k = int(x/2)
lst1 = []
lst2 = []
ls = []
if x%2==0:
    for i in range(n+1):
        ls.append(True)
    while k>0:
        if k<=n:
            lst1.append(k)
            ls[k] = False
            k = 0
        else:
            lst1.append(n)
            ls[n] = False
            k = k - n
            n-=1
    for i in range(1,n+1):
        if ls[i]==True:
            lst2.append(i)
    lst1.sort()
    print("YES")
    print(len(lst1))
    print(*lst1)
    print(len(lst2))
    print(*lst2)
else:
    print("NO")
