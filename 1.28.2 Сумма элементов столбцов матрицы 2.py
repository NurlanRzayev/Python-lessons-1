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

s=[0]*M#это массив для хранения сумм столбцов
for i in range(N):
    for j in range(M):
        s[j]+=A[i][j]#массив s сначала заполняется элементами первой строки , затем на каждой итерации внешнего цикла к каждому элементу s прибавляется соответствующий элемент строки А (т.е. соотв. элемент списка , кот. находится внутри списка А)

print(s)