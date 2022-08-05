A=[1,8,6,7,3]
B=[]

for i in enumerate(A):
    B.append(str(i[0])+' '+str(i[1]))

print(B)