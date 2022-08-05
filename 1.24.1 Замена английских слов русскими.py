ru=['один','два','три','четыре','пять']

f1=open('data.txt')
f2=open('dataRu.txt','w')

i=0 # индексы для ru
for line in f1: # построчно считывает данные файла , см. # в след. программе
    l=line.split()
    l[0]=ru[i]
    i+=1
    l=' '.join(l)
    f2.write(l)

f1.close()
f2.close()