n = int(input())

if n < 0:
    print("Ошибка")
else:
    count = 0
    total = 0
    
    if n == 0:
        count = 1
    else:
        while n > 0:
            total += n % 10
            count += 1
            n //= 10
            
    print(f"Цифр: {count}")
    print(f"Сумма цифр: {total}")