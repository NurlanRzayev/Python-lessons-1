a_str=input('Value 1: ')
b_str=input('Value 2: ')

try:
    a_num=float(a_str)
    b_num=float(b_str)
    print('Result: ' , a_num+b_num)
except ValueError:
    print('Result: ' , a_str+b_str)

# Ecли в данной программе не задавать новые переменные то программа будет работать
# в 3 случаях из 4 , но в 1 когда пользователь ввел сперва число потом к примеру
# букву то попытка их сложения приведет к исключению TypeError