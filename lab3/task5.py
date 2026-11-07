identifier = input()

length = len(identifier)
is_alpha = identifier.isalpha()
is_digit = identifier.isdigit()
is_alnum = identifier.isalnum()
has_dash = "-" in identifier

print(f"Длина: {length}")
print(f"Только буквы: {is_alpha}")
print(f"Только цифры: {is_digit}")
print(f"Буквенно-цифровая: {is_alnum}")
print(f"Содержит дефис: {has_dash}")