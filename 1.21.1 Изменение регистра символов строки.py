s=input()

n_small=0
n_big=0

for i in s:
    if i.islower():
        n_small+=1
    elif i.isupper():
        n_big+=1

if n_small>=n_big:
    print(s.lower())
else:
    print(s.upper())