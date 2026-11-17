n = int(input())

if n < 2:
    print("Ошибка")
else:
    d = 2
    first = True
    while d * d <= n:
        while n % d == 0:
            if not first:
                print(" ", end="")
            print(d, end="")
            first = False
            n //= d
        d += 1
    
    if n > 1:
        if not first:
            print(" ", end="")
        print(n, end="")
    print()