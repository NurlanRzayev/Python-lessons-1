a=input('Value 1: ')
b=input('Value 2: ')

try:
    print(float(a)+float(b))
except ValueError:
    print('Result: ' , a+b)
