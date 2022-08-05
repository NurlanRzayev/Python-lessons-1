a=input('Value 1: ')
b=input('Value 2: ')

try:
    a=int(a)
except ValueError:
    print('Resultat: ' , a+b)
else:
    try:
        b=int(b)
    except ValueError:
        a=str(a)
    finally:
        print('Result: ' , a+b)