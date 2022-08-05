N=5
words=['']*N
length=[0]*N

for i in range(N):
    words[i]=input()
    length[i]=len(words[i])

print(words)
print(length)