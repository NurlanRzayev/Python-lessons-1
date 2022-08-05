f=open('nums.txt')
n=f.read() # считываются все данные в одну строку
n=n.split()
for i in range(len(n)):
    n[i]=int(n[i])
print(sum(n))