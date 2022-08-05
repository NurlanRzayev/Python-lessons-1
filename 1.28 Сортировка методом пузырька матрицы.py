from random import randint

N=3
M=4

def output_matrix(matrix):#функция вывода мотрицы на экран
    for row in matrix:
        for item in row:
            print('%3d' %item,end='')
        print()

A=[]
for i in range(N):#создаем матрицу
    a=[]
    for j in range(M):
        a.append(randint(1,99))
    A.append(a)

output_matrix(A)
print()

for i in range(N):
    for j in range(M-1):#см. "Сортировка методом пузырька"
        for k in range(M-j-1):
            if A[i][k]>A[i][k+1]:
                A[i][k],A[i][k+1]=A[i][k+1],A[i][k]

output_matrix(A)