a=input('Value 1: ')
b=input('Value 2: ')

try:
    a=float(a)
    b=float(b)
    print('Result: ' , a+b)
except ValueError:
    try:
        print('Result: ' , a+b)
    except TypeError:
        a=int(a)#к примеру пользователь ввел 9 , float вернул 9.0 , int обратно преобразовал в 9
        a=str(a)#здесь получаем строку '9' а не '9.0'
        print('Result: ' , a+b)
