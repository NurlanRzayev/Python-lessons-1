def mult():
    mult=1
    n=int(input())
    if n==0:
        mult=0
    while n!=0:
        mult*=n
        n=int(input())
    return mult

print(mult())
