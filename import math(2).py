import math
raw_data = input("Введите строку данных через('|'): ")
fields = raw_data.split("|")
tank_field = fields[0].strip()
diameter_field = fields[1].strip()
height_field = fields[2].strip()
tank_name = tank_field.split("=")
[1].strip().title()
#Диаметер
diameter_str = diameter_field.split("=")
[1].replace("m", "").strip()
diameter = float(diameter_str)
#Высота
height_str = height_field.split("=")
[1].replace("m", "").strip()
height = float(height_str)
#радиус
radius = diameter/2
volume = math.pi*math.pow(radius, 2)*height
volume_floor = math.floor(volume)
print()
print("="*15, "ОТЧЁТ ПО ЁМКОСТИ", "="*15)
print("Ёмкость", tank_name, sep=":", end="\n")
print(f"Диаметр: {diameter:>12.2f} м")
print(f"Радиус: {radius:>12.2f} м")
print(f"Высота: {height:>12.2f} м")
print(f"объём (точный): {volume:>12.2f}")
print(f"объём (округл. вниз): {volume_floor:>12.2f} м")
print("="*48) 