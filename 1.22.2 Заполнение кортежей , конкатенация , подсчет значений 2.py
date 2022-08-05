from random import randint

def fill_tuple(a,b):
    l=[]
    for i in range(10):
        l.append(randint(a,b))
    return tuple(l)

first=fill_tuple(0,5)
second=fill_tuple(-5,0)
third=first+second
count_zero=third.count(0)

print(third)
print(count_zero)