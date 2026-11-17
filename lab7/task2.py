s = input()
original = list(map(int, s.split())) if s else []

squares = [x * x for x in original if x > 0 and x % 2 != 0]

print(f"Квадраты: {squares}")