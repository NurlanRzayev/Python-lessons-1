from random import randint

def f(l,a,b):
    i=0
    while i<10:
        l.append(randint(a,b))
        i=i+1
        t=tuple(l)
    return t

t1=f([],0,5)
t2=f(l=[],a=-5,b=0)
t3=t1+t2
print(t3)
print(t3.count(0))