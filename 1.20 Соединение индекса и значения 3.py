A=[2,7,3,7,3]
B=[]

for i in enumerate(A):
    B.append('{} {}'.format(i[0],i[1]))

print(B)