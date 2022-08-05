def getinput():
    s=input()
    return s

def testinput(s):
    try:
        n=int(s)
        return True
    except ValueError:
        return False

def strtoint(s):
    n=int(s)
    return n

def printint(n):
    print(n)

s1=getinput()
if testinput(s1):
    printint(strtoint(s1))