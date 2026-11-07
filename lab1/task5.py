distance = 250
fuel_consumption = 7.5 
fuel_price = 60 

fuel_needed = distance * fuel_consumption / 100
total_cost = fuel_needed * fuel_price

print(f"Топливо: {fuel_needed:.2f} л")
print(f"Стоимость: {total_cost:.2f} руб")