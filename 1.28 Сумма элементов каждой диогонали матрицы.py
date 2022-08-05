from random import randint

N=5

A=[]#создаем и выводим матрицу
for i in range(N):
    a=[]
    for j in range(N):
        n=randint(1,9)
        a.append(n)
        print('%3d' %n,end='')
    A.append(a)
    print()

diagonal1=0
diagonal2=0
for i in range(N):
    diagonal1+=A[i][i]
    diagonal2+=A[i][N-1-i]#индекс столбца каждого элемента побочной диагонали начиная с левого верхнего края уменьшается на число увеличивающееся с шагом 1 , также как i после каждой итерации

print(diagonal1)
print(diagonal2)