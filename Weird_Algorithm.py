n = int(input())
ls = []
while True:
    ls.append(n)
    if n==1:
        break
    elif n%2==1:
        n = n*3+1
    else:
        n = int(n/2)
print(*ls)
