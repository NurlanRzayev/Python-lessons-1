import random

def output_list(lst):
    i=1
    while i<=100:
        print('% .2f'%lst[i-1],end=' ')
        if i%10==0:
            print()
        i+=1

a=[]
i=0
while i<100:
    a.append(random.random())
    i+=1

output_list(a)
a.sort()
print()
output_list(a)