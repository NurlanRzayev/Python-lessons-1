a=input('Value 1: ')
b=input('Value 2: ')

try:
    a=int(a)
    b=int(b)
except ValueError:
    pass

if type(a)==int and type(b)==str:
    a=str(a)

print('Result: ' , a+b)