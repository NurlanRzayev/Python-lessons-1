a = int(input())
b = int(input())

if a > b:
    A = []
    n = b
    while n <= a:
        A.append(n)
        n += 1
    
    f_A = filter(lambda i: i % b == 0, A)
    print(list(f_A))

