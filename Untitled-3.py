customer_name = input("ВВедите имя клиента: ")
car_brand = input("Введите марку автомобиля: ")
rent_price_per_day = float(input("Введите стоимость аренды за сутки: "))
days_count = int(input("Введите количество суток аренды: "))
extra_service_price = float(input("Введите стоимость одной дополнительной услуги: "))
extra_service_count = int(input("Введите количество дополнительных услуг: "))

rent_cost = rent_price_per_day*days_count
extra_cost = extra_service_price*extra_service_count
total_cost = rent_cost + extra_cost
average_per_day = total_cost/days_count

print()
print("="*35)
print("ДОГОВОР АРЕНДЫ АВТОМОБИЛЯ")
print("="*35)
print("Клиент", customer_name, sep=":", end="\n")
print("Автомобиль", car_brand, sep=":", end="\n")
print("-"*35)
print(f"Стоимость аренды за сутки:{rent_price_per_day:2f}руб.")
print(f"Колличество суток: {days_count}шт.")
print(f"Стоимость аренды:{rent_cost:.2f}руб.")
print("-"*35)
print(f"Цена доп. услуги:{extra_service_price:.2f}руб.")
print(f"Колличество доп. услуг:{extra_service_count} шт.")
print(f"Стоимость доп. услуг:{extra_cost:.2f}руб.")
print("-"*35)
print(f"ИТГО К ОПЛАТЕ:{total_cost:.2f}руб.")
print(f"Средняя стоимость за сутки:{average_per_day:2f}руб.")
print("="*35)
print("Спасибо за обращение!")
