a = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (3, 2, 1)]

for i in a:
    for j in i:
        print('%3d' %j, end=' ')
    print()

for i in zip(*a):
    print('%3d' %sum(i), end=' ')