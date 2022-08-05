def swap_key_value(d1):
    d2 = {}
    for key, value in d1.items(): # здесь key, value это простые переменные такие же как i, j
        d2[value] = key
    return d2


a = {1: 'one', 2: 'two', 3: 'three'}
b = swap_key_value(a)

print(a)
print(b)