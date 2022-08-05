n = int(input('Предел: '))
a = int(input('Кратны числу: '))
r = filter(lambda i: i % a == 0, range(1, n))
print(list(r))