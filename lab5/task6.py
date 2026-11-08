n = int(input())

odd_count = 0

for r in range(n):
    c = 1
    print(c, end="")
    if c % 2 == 1:
        odd_count += 1

    for k in range(r):
        c = c * (r - k) // (k + 1)
        print(" " + str(c), end="")
        if c % 2 == 1:
            odd_count += 1

    print()

print(f"Нечетных элементов: {odd_count}")