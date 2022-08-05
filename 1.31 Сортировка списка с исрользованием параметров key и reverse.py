a=[['John',10,130,35],['Bill',11,135,39],['Max',9,120,33],['William',10,128,30]]
n=input('Sort by name(0) , by age(1) , by height(2) , by weight(3): ')
t=int(input('By ascending(0) , by descending(1): '))
b=sorted(a,key=lambda item:item[int(n)],reverse=bool(t))
for i in b:
    print('%7s%3d%4d%3d'%(i[0],i[1],i[2],i[3]))