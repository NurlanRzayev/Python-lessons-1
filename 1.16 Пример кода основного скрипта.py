import square

figure=input('Rectangle-1,triangle-2,circle-3: ')

if figure=='1':
    a=float(input('Width: '))
    b=float(input('Height: '))
    print(square.rectangle(a,b))
elif figure=='2':
    a=float(input('Base: '))
    h=float(input('Height: '))
    print(square.triangle(a,h))
elif figure=='3':
    r=float(input('Radius: '))
    print(square.circle(r))
else:
    print('Input error')

# После запуска программы, где импортируется другая программа как модуль, в папке где они лежат появляется папка __pycache__