a=input('Value 1: ')
b=input('Value 2: ')

try:
    a=int(a)
    b=int(b)
    print('Result: ' , a+b)
except ValueError:
    a=str(a)
    print('Result: ' , a+b)