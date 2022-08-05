try:
    old=int(input('Ваш возраст: '))
except ValueError:
    print('Ошибка ввода')
    quit()

print('Рекомендовано: ', end='')

if 3<=old<6:
    print('"Заяц в лабиринте"')
elif 6<=old<12:
    print('"Марсианин"')
elif 12<=old<16:
    print('"Загадочный остров"')
elif 16<=old:
    print('"Поток сознания"')
else:
    print('-')