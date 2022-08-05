d={'+':(lambda i,j:i+j),'-':(lambda i,j:i-j),'*':(lambda i,j:i*j),'/':(lambda i,j:i/j)}
a=int(input())
b=int(input())
for i in list(d.values()):
    print(i(a,b))