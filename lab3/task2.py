full_name = input()

parts = full_name.split()

surname = parts[0].capitalize()
initial_name = parts[1][0].upper() + "."
initial_patronymic = parts[2][0].upper() + "."

print(f"{surname} {initial_name} {initial_patronymic}")