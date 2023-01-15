n = input()
n = int(n)
while True:
    print(n)
    if(n==1):
        break
    elif n%2==1:
        n  = n * 3 + 1
    else:
        n = n / 2
        n = int(n)
