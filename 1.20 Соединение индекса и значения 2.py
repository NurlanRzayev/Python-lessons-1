A=[2,9,5,4]
B=[]

for i in enumerate(A):
    B.append('%d %d' %(i[0],i[1]))

print(B)