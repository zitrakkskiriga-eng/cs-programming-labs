s = input()
original = list(map(int, s.split())) if s else []
fixed = original.copy()

for i in range(len(fixed)):
    if fixed[i] < 0:
        fixed[i] = 0

print(f"Исходные остатки: {original}")
print(f"Исправленные остатки: {fixed}")