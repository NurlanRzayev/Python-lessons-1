s=input()
if len(s)>10:
    print('Warning')
else:
    diff=10-len(s)
    s=s+'*'*diff
    print(s)