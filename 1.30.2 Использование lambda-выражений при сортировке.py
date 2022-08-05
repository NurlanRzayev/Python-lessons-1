l=['apple','banana','orange','tomato','soup']
l.sort(key=lambda i:i[-1])
print(l)
l.sort(key=lambda i:len(i))#a.sort(key=len)
print(l)