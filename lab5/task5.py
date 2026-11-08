count = 0
total = 0

while True:
    s = input()
    if s == "stop":
        break
    cost = int(s)
    count += 1
    total += cost

if count == 0:
    print("Нет покупок")
else:
    print(f"Покупок: {count}")
    print(f"Общая стоимость: {total} руб")
    print(f"Средняя стоимость: {total / count:.2f} руб")