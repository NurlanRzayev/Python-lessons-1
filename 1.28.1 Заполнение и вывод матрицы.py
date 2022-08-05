from random import randint

N=3
M=4

A=[]
for i in range(N):
    a=[]
    for j in range(M):
        a.append(randint(-9,9))
    A.append(a)

for i in range(N):
    for j in range(M):
        if A[i][j]>=0:
            print('%2d' %A[i][j],end='')
        else:
            print('%2s' %'-',end='')
    print()