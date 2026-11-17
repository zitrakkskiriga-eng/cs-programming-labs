s = input()
original = list(map(int, s.split())) if s else []
target = int(input())

indices = [i for i, x in enumerate(original) if x == target]

print(f"Индексы: {indices}")