from random import randint

N = 3 # количество массивов, строк матрицы
M = 4 # количество элементов в одном массиве, столбцов матрицы

A = [] # матрица
for i in range(N): # в этом цикле создаем матрицу
    a = [] # массив, строка матрицы
    for j in range(M):
        a.append(randint(1, 99))
    A.append(a)

print(A, end='\n\n') # вывод матрицы в одну строку и отступ на одну пустую строку по вертикали

for i in range(N): # в этом цикле выводим матрицу на экран в классическом ее виде
    for j in range(M):
        print('%3d' %A[i][j], end='')
    print() # деактивация последнего end='' в цикле для j, чтобы каждый последующий цикл для i печатал с новой строки