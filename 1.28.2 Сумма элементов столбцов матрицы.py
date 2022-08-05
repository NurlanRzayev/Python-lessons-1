from random import randint

N=5
M=4

A=[]
for i in range(N):
    a=[]
    for j in range(M):
        n=randint(1,99)
        a.append(n)
        print('%4d' %n,end='')
    A.append(a)
    print()

print()

s=0
for j in range(M):
    for i in range(N):
        s+=A[i][j]
    print('%4d' %s,end='')

print()