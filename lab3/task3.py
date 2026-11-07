phone = input()

clean_phone = phone.replace("+", "")
clean_phone = clean_phone.replace(" ", "")
clean_phone = clean_phone.replace("(", "")
clean_phone = clean_phone.replace(")", "")
clean_phone = clean_phone.replace("-", "")

print(clean_phone)